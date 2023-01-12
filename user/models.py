from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    full_name = models.CharField(max_length=128)
    phongban = models.ForeignKey("user.PhongBan", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name.__str__()

    def get_absolute_url(self):
        return reverse('user_detail', args=[self.username.__str__()])


class PhongBan(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name.__str__()
