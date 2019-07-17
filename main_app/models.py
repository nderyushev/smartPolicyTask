from django.db import models
from django.contrib.auth.models import User


class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.keyword


class Video(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='videos')
    url = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.url
