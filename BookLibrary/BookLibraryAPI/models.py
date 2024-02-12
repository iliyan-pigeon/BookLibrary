from django.db import models


class Books(models.Model):
    headline = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    author = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    amount_in_stock = models.PositiveIntegerField(
        default=1,
        null=False,
        blank=False,
    )
    description = models.CharField(
        max_length=500,
        default="None",
        null=False,
        blank=False,
    )
