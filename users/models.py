from django.db import models
from django.contrib.auth.models import User
from .managers import EntryManager
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Hi I have not filled my Bio Yet')
    SearchEntry = EntryManager()

    def __str__(self):
        return f'{self.user.username} Profile'


