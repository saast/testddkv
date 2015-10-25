from django.db import models

class Tenant(models.Model):
    lastname = models.TextField(default='')

class Estate(models.Model):
    address = models.TextField(default='')
