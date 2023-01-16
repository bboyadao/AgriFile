from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    full_name = models.CharField(max_length=128)
    phongban = models.ForeignKey("setmeup.PhongBan", on_delete=models.PROTECT)
    title = models.ForeignKey("setmeup.Title", on_delete=models.PROTECT)

    def get_my_user_name(self):
        if self.username.startswith(settings.USER_IMPORT_PREFIX):
            return None
        return self.username

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"{self.full_name.__str__() or self.username}.....{self.phongban.name}"

    @property
    def get_absolute_url(self):
        return reverse('user_detail', args=[self.pk])
