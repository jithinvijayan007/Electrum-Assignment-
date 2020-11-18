from django.db import models

# Create your models here.

class MoviesModel(models.Model):

    title = models.CharField(max_length = 210, null=False, blank = False)
    released_year = models.IntegerField(null = False, blank = False)
    rating = models.DecimalField(decimal_places = 1, max_digits = 2)
    id = models.CharField(max_length = 118, primary_key = True)
    genres = models.CharField(max_length = 118, null=False, blank = False)

    def __str__(self):
        return self.title
