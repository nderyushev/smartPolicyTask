import logging
import aiohttp
import asyncio
import json

from asgiref.sync import async_to_sync

from smart_policy_task.celery import app
from custom_config import API_KEY
from main_app.models import Keyword, Video


async def get_videos_for_query(query):

    async with aiohttp.ClientSession() as session:
        async with session.get(
        'https://www.googleapis.com/youtube/v3/search', 
        params={
            'part': 'snippet',
            'q': query,
            'key': API_KEY      
        }) as resp:
            print('@@@@@@@@@@@@@@@@', resp.url, resp.status)
            return await resp.json()


async def save_videos_for_query(query):

    videos_json = await get_videos_for_query(query.keyword)

    current_videos = Video.objects.filter(keyword__keyword=query)
    current_videos_urls = list(map(lambda x: x.url, current_videos))

    for video in videos_json['items']:
        
        video_id = video['id'].get('videoId')
        video_url = f'https://www.youtube.com/watch?v={video_id}' 

        if not video_id or video_url in current_videos_urls:
            continue

        async with aiohttp.ClientSession() as session:
            await session.post(
            f'http://127.0.0.1:8000/api/words/{query.id}/video',
                data={
                    'url': f'https://www.youtube.com/watch?v={video_id}',
                    'published_date': video['snippet']['publishedAt']
            })

@app.task
def update_videos_list():
    queries = Keyword.objects.all()
    
    for query in queries:
        async_to_sync(save_videos_for_query)(query)
