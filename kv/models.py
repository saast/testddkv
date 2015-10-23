from django.db import models

class Tenant(models.Model):
    lastname = models.TextField(default='')
