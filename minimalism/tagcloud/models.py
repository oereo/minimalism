from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):

    STATUS_TYPES = [
        (1, '생필품'),
        (2, '문구류'),
        (3, '주방용품'),
        (4, '전자기기'),
        (5, '의류'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='유저')
    title = models.CharField(max_length=127)
    content = models.CharField(max_length=255)
    clean_date = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=63, choices=STATUS_TYPES, default=1)
