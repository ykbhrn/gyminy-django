from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Like(models.Model):
  owner = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
  image = models.ForeignKey('images.Image', related_name='likes', on_delete=models.CASCADE, null=True, blank=True)
  video = models.ForeignKey('videos.Video', related_name='likes', on_delete=models.CASCADE, null=True, blank=True)
  article = models.ForeignKey('articles.Article', related_name='likes', on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return f'Like {self.id}'