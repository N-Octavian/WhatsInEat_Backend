from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=512, unique=True)
    description = models.TextField(unique=False, blank=True)
