from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    detail = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
