from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    full_name = models.CharField(max_length=128)
    phongban = models.ForeignKey("setmeup.PhongBan", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.full_name.__str__()

    @property
    def get_absolute_url(self):
        return reverse('user_detail', args=[self.username.__str__()])
