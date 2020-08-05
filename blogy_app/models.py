from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserDetail(AbstractUser):
    bio = models.CharField(max_length=500)
    image_src = models.CharField(max_length=100)

    def __str__(self):
        return self.username
