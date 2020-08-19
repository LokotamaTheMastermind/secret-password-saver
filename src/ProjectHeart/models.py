from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Passwords(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    website_name = models.CharField(max_length=100, default="Example Site", blank=False, null=False, verbose_name="Site Name", unique=True)
    website_url = models.URLField(blank=False, null=False, max_length=100, verbose_name="Site URI", default="https://www.domain.com/")
    password = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Password (Actual)", unique=True)
    password_hashed = models.CharField(max_length=1500, null=True, blank=True, default="No hashed password", verbose_name="Password (Hashed)")

    class Meta:
        verbose_name_plural = "Passwords"

    def __str__(self):
        return self.website_name

    def save(self, *args, **kwargs):
        if self.password:
            pwd = make_password(self.password)[:30]
        self.password_hashed = str(pwd)
        super().save(*args, **kwargs)
