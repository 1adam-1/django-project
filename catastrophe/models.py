from django.db import models

class Catastrophe(models.Model):
    nom = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='photos/')
    text = models.TextField()


