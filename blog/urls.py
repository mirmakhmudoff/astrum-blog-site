from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListView.as_view()),
    path('articles/<int:id>/', views.ArticleDetailView.as_view()),
    path('videos/', views.VideoListView.as_view()),
    path('audios/', views.AudioListView.as_view()),
    path('images/', views.ImageListView.as_view()),
    path('comments/', views.CommentListView.as_view()),
]
