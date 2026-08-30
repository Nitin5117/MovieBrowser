from django.db import models
from django.contrib.auth.models import User


class Cast(models.Model):
    id = models.CharField(max_length=255, primary_key=True) 
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    profile_path = models.URLField(max_length=500, blank=True, null=True)
    popularity = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} as {self.character}"
class Movie(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    original_title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=50, blank=True, null=True) 
    overview = models.TextField()
    poster_path = models.URLField(max_length=500, blank=True, null=True)
    backdrop_path = models.URLField(max_length=500, blank=True, null=True)
    original_language = models.CharField(max_length=20)
    vote_average = models.FloatField(default=0.0)
    vote_count = models.IntegerField(default=0)
    popularity = models.FloatField(default=0.0)

    casts = models.ManyToManyField(Cast, related_name='movies', blank=True)

    user = models.ManyToManyField(User,related_name="Watchlist" , blank=True)

    

    def __str__(self):
        return self.original_title
  
