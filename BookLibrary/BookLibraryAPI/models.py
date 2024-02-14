from django.contrib.auth.models import AbstractUser
from django.core import validators
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


class BooksUser(AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    GENDER_MAX_LENGTH = 1

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        ),

    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
        ),
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=GENDER_MAX_LENGTH,
        choices=GENDER_CHOICES,
    )
