from django.contrib.auth.models import User
from rest_framework import serializers

from .models import News


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class NewsListSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField('get_views')
    photo = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = News
        fields = ('id', 'title', 'summary', 'photo', 'video_url', 'rank', 'views', 'created_at')

    def get_views(self, obj):
        return obj.view_records.count() + 1

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None


class NewsDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    views = serializers.SerializerMethodField('get_views')
    photo = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = News
        fields = ('id', 'author', 'title', 'summary', 'content', 'photo', 'video_url', 'rank', 'views', 'created_at')

    def get_views(self, obj):
        return obj.view_records.count() + 1

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None
