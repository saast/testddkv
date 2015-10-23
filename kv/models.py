from django.db import models

class Item(models.Model):
    lastname = models.TextField(default='')
