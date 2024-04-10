from django.db import models
from django.conf import settings
from django.urls import reverse

class StreamPlatform(models.Model):

    name = models.CharField(max_length=70)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
    

class WatchList(models.Model):

    title = models.CharField(max_length=50)
    movie_poster = models.FileField(upload_to='img/', default=None, null=True, max_length=250, blank=True)
    storyline = models.CharField(max_length=70)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="movie_list")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title