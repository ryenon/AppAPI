from django.db import models

# Create your models here.

class Game (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True)
    played = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
