from django.db import models

class recipes(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/')
    ingredients = models.TextField(max_length=100)
    recipe = models.TextField(max_length=500)
