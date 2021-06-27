from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=200)
