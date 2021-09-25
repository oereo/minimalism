from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='유저')
    title = models.CharField(max_length=127)
    content = models.CharField(max_length=255)
    clean_date = models.CharField(max_length=15, null=True)
