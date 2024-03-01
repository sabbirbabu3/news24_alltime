from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

CATEGORY_RATINGS = [
    (1, '*'), 
    (2, '* *'), 
    (3, '* * *'), 
    (4, '* * * *'),
]
class Categories(models.Model):
    name=models.CharField(max_length=20)
    slug=models.SlugField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    category = models.ManyToManyField(Categories)
    publishing_time = models.DateTimeField(default=timezone.now)
    

    def __str__(self) -> str:
        return self.headline
    

class ArticleRating(models.Model):
   
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=CATEGORY_RATINGS)
    created_at = models.DateTimeField(default=timezone.now)


