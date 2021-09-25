from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='유저')
    nickname = models.CharField(max_length=63, null=True, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
