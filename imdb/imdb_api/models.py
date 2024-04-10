from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    

class Review(models.Model):
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    desc = models.CharField(max_length=100)
    WatchList = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        string = str(self.rating) + " " + self.WatchList.title
        return string