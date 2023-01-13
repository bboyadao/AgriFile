from django.db import models
from django.urls import reverse


class PhongBan(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name.__str__()


class NoiNhan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name.__str__()

    @property
    def get_absolute_url(self):
        return reverse('noinhan_detail', args=[self.pk.__str__()])


class LichBaoCao(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name.__str__()

    @property
    def get_absolute_url(self):
        return reverse('lichbaocao_detail', args=[self.pk.__str__()])