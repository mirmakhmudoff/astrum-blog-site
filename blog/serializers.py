from rest_framework import serializers
from .models import Article, TechnicalArticle, NewsArticle, Video, Audio, Image, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'type', 'author', 'created_at']

class TechnicalArticleSerializer(ArticleSerializer):
    class Meta(ArticleSerializer.Meta):
        model = TechnicalArticle

class NewsArticleSerializer(ArticleSerializer):
    class Meta(ArticleSerializer.Meta):
        model = NewsArticle

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'duration', 'uploaded_at']

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'title', 'description', 'url', 'duration', 'uploaded_at']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'description', 'url', 'width', 'height', 'uploaded_at']


class CommentSerializer:
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'article_id', 'created_at', 'is_approved']
