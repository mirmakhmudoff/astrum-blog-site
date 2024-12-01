from django_filters import rest_framework as filters
from .models import Article, MultimediaContent

class ArticleFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    type = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'type']

class MultimediaFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = MultimediaContent
        fields = ['title', 'description']