from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    full_name = models.CharField(max_length=128)
    phongban = models.ForeignKey("setmeup.PhongBan", on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey("setmeup.Title", on_delete=models.SET_NULL, null=True)

    def get_my_user_name(self):
        if self.username.startswith(settings.USER_IMPORT_PREFIX):
            return None
        return self.username

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.full_name.__str__()

    @property
    def get_absolute_url(self):
        return reverse('user_detail', args=[self.pk])
