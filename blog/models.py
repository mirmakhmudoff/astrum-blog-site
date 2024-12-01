from django.db import models


class Article(models.Model):
    TYPES = (
        ('article', 'Article'),
        ('technical', 'Technical'),
        ('news', 'News'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(choices=TYPES, max_length=20)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def article_factory(type, **kwargs):
    if type == 'technical':
        return TechnicalArticle.objects.create(**kwargs)
    elif type == 'news':
        return NewsArticle.objects.create(**kwargs)
    else:
        return Article.objects.create(**kwargs)


class TechnicalArticle(Article):
    tech_details = models.TextField()


class NewsArticle(Article):
    source = models.CharField(max_length=100)


class MultimediaContent(models.Model):
    TYPES = (
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('image', 'Image'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(choices=TYPES, max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Video(MultimediaContent):
    url = models.URLField()
    duration = models.DurationField()


class Audio(MultimediaContent):
    url = models.URLField()
    duration = models.DurationField()


class Image(MultimediaContent):
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.article.title}'