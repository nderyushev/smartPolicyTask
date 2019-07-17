from rest_framework import generics, mixins, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from main_app.models import Keyword, Video
from main_app.api.serializers import KeywordSerializer, VideoSerializer
from main_app.api.pagination import SmallSetPagination


class KeywordListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        user = self.request.user
        return Keyword.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class KeywordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer 

    permission_classes = [
        IsAuthenticated
    ]

class VideoListAPIView(generics.ListCreateAPIView):
    # queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        keyword_pk = self.kwargs.get("word_pk")
        return Video.objects.filter(keyword_id=keyword_pk).order_by('-id')

    def perform_create(self, serializer):
        keyword_pk = self.kwargs.get("word_pk")
        keyword = get_object_or_404(Keyword, pk=keyword_pk)
        serializer.save(keyword=keyword)

