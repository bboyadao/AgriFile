from django.db import models
from django.urls import reverse
from django.utils import timezone


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
    duedate = models.DateTimeField(null=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.name.__str__()

    @property
    def get_absolute_url(self):
        return reverse('lichbaocao_detail', args=[self.pk.__str__()])

    @property
    def get_delta_days(self):
        return (self.duedate - timezone.now()).days

    @property
    def get_class_by_time(self):
        delta = self.get_delta_days
        classs = ""

        if delta <= 7:
            classs = "callout-danger"

        elif delta <= 14:
            classs = "callout-warning"

        elif delta <= 21:
            classs = "callout-info"
        else:
            classs = "callout-success"

        return classs