from typing import List

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import News, NewsCategory, NewsPhoto


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'title',)


class NewsListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    url: str = serializers.SerializerMethodField('get_url')
    views: int = serializers.SerializerMethodField('get_views')
    photo: str = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = News
        fields = ('id', 'category', 'title', 'slug', 'url', 'summary', 'photo', 'video_url', 'rank', 'views', 'created_at')

    def get_url(self, obj) -> str:
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_absolute_url())

    def get_views(self, obj) -> int:
        return obj.view_records.count() + 1

    def get_photo_url(self, obj) -> str | None:
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None


class CategoryListWithNewsSerializer(serializers.ModelSerializer):
    url: str = serializers.SerializerMethodField('get_url')
    news_count: int = serializers.SerializerMethodField('get_news_count')
    news_list: list[NewsListSerializer] = serializers.SerializerMethodField('get_news_list')

    class Meta:
        model = NewsCategory
        fields = ('id', 'title', 'slug', 'url', 'news_count', 'news_list')

    def get_url(self, obj) -> str:
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_absolute_url())

    def get_news_count(self, obj) -> int:
        return obj.news_set.filter(is_active=True).count()

    def get_news_list(self, obj) -> list[NewsListSerializer]:
        news_list = obj.news_set.filter(is_active=True).order_by('-created_at')[:4]
        return NewsListSerializer(news_list, many=True, context={'request': self.context.get('request')}).data


class CategoryRelatedNewsListSerializer(serializers.ModelSerializer):
    news_count: int = serializers.SerializerMethodField('get_news_count')
    news_list: list[NewsListSerializer] = serializers.SerializerMethodField('get_news_list')

    class Meta:
        model = NewsCategory
        fields = ('id', 'title', 'slug', 'news_count', 'news_list')

    def get_news_count(self, obj) -> int:
        return obj.news_set.filter(is_active=True).count()

    def get_news_list(self, obj) -> list[NewsListSerializer]:
        news_list = obj.news_set.filter(is_active=True).order_by('-created_at')
        return NewsListSerializer(news_list, many=True, context={'request': self.context.get('request')}).data


class NewsPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPhoto
        fields = ('photo',)

    def to_representation(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None


class NewsDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    views: int = serializers.SerializerMethodField('get_views')
    photo: str = serializers.SerializerMethodField('get_photo_url')
    photos: list = serializers.SerializerMethodField('get_photos', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'category', 'author', 'title', 'slug', 'url', 'summary', 'content', 'content2', 'photo', 'photos', 'video_url', 'rank', 'views', 'created_at')

    def get_views(self, obj) -> int:
        return obj.view_records.count() + 1

    def get_photo_url(self, obj) -> str | None:
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None

    def get_photos(self, obj) -> List[str | None]:
        photos = obj.photos.all()
        return NewsPhotosSerializer(photos, many=True, context={'request': self.context['request']}).data
