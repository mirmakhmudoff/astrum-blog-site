from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Article, Video, Audio, Image, Comment
from .serializers import ArticleSerializer, VideoSerializer, AudioSerializer, ImageSerializer, CommentSerializer
from .pagination import ArticlePagination
from rest_framework.permissions import IsAuthenticated
from .filters import ArticleFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    filterset_class = ArticleFilter
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class VideoListView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

class AudioListView(generics.ListCreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

class ImageListView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
