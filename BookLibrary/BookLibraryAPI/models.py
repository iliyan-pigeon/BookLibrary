from django.db import models


class Books(models.Model):
    headline = models.CharField(
        max_length=200
    )
    author = models.CharField(
        max_length=200
    )
