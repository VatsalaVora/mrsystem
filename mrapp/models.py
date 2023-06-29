from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    Movie_Title = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)
    Year = models.IntegerField(null=True)
    Actors = models.CharField(max_length=100)
    Rating = models.FloatField()
    Runtime = models.CharField(max_length=100)
    Censor = models.CharField(max_length=100)
    Total_Gross = models.CharField(max_length=100)
    main_genre = models.CharField(max_length=100)
    side_genre = models.CharField(max_length=100)

    def __str__(self):
        return self.Movie_Title
