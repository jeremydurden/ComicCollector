from django.db import models

class Comic(models.Model):
    name = models.CharField(max_length=100)
    issue = models.IntegerField()
    writer = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


