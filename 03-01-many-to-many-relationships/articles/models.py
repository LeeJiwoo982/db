from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # '좋아요' 기능은 게시글에 달려서 
    # 매니투매니필드는 게시글모델에 작성
    # 단순 복수형 이름보다 
    # 만들려는 기능이 무엇인지 생각하고 명시적인 매니저 이름을 설정하기
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
