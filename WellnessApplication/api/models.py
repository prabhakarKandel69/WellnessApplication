from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', "Male"), ("female", "Female")], null=True, blank=True)
    height = models.FloatField(help_text="In centimeters", null=True, blank=True)
    weight = models.FloatField(help_text="In kgs", null=True, blank=True)
    self_reported_stress = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Stress level from 1-10",
        null=True,
        blank=True
    )
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']