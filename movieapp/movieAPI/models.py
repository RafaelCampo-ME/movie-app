from django.db import models


class Movie(models.Model):
    """movie models

    Description:
        models contains the basic info of the movie

    """
   #class PegiClasifi(models.IntegerChoices):
   #    PEGI_3 = 3
   #    PEGI_7 = 7
   #    PEGI_12 = 12
   #    PEGI_16 = 16
   #    PEGI_18 = 18




    id = models.IntegerField(primary_key=True)
    entry_creation_datetime = models.DateTimeField(auto_now_add=True)
    entry_updated_datetime = models.DateTimeField()
    title = models.TextField(max_length=120)
    director_name = models.TextField(max_length=80)
    premier_date = models.DateField()
    movie_projection_time_slot = models.JSONField(blank=True, null=True)
    ticket_price = models.FloatField()
    sinopsis = models.TextField(max_length=300)
    img_path = models.TextField(max_length=300)
    pegi = models.IntegerField()
    genre = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title


