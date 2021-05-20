from django.db import models

# Create your models here.
from django.db import models

# 코드 수정 부분 (추가)
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정

    def __str__(self):
        return f"[{self.pk}] {self.title}"
