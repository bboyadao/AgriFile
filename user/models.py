from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=128)
    phongban = models.ForeignKey("user.PhongBan", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name.__str__()


class PhongBan(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name.__str__()
