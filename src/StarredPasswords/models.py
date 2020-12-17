from django.db import models
from ProjectHeart.models import Passwords


class StarredPasswords(models.Model):
    password = models.ForeignKey(Passwords, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Starred Passwords'
