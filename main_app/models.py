from django.db import models
from django.urls import reverse

class Hero(models.Model):
  name = models.CharField(max_length=50)
  secret_identity = models.CharField(max_length=50)
  power = models.TextField(max_length=250)

  def __str__(self):
    return f'{self.name} is truly {self.secret_identity} with the power(s) of {self.power}'

  def get_absolute_url(self):
    return reverse('heroes_detail', kwargs={'pk': self.id})


class Comic(models.Model):
    name = models.CharField('Title', max_length=100)
    issue = models.IntegerField('Issue No:')
    writer = models.CharField('Writer(s)', max_length=100)
    artist = models.CharField('Artist(s)', max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})

class Cover(models.Model):
    image = models.CharField('Cover Image URL', max_length=100)
    artist = models.CharField(max_length=100)

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image} was illustrated by {self.artist}"