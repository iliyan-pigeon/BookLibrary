from django.db import models


class Books(models.Model):
    headline = models.CharField(
        max_length=200
    )
    author = models.CharField(
        max_length=200
    )
    amount_in_stock = models.PositiveIntegerField(
        default=1,
        null=False,
        blank=False,
    )