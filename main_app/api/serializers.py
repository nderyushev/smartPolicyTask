from rest_framework import serializers, fields
from main_app.models import Keyword, Video


class VideoSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    keyword = serializers.ReadOnlyField(source='keyword.keyword')
    published_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])

    class Meta:
        model = Video
        fields = "__all__"
        # exclude = ("keyword",)


class KeywordSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Keyword
        fields = "__all__"
        extra_kwargs = {'user': {'required': False}}

