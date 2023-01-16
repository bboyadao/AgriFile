from django.db import models
from django.urls import reverse
from django.utils import timezone


class Title(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name.__str__()


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
    class Loai(models.IntegerChoices):
        khan = 1, "Khẩn"
        dotxuat = 2, "Đột xuất"
        dinhky = 3, "Định kỳ"

    class DinhKy(models.IntegerChoices):
        thang = 1, "Tháng"
        quy = 2, "Quý"
        nam = 3, "Năm"
        six = 4, "6 tháng"
        nine = 5, "9 tháng"

    name = models.CharField(max_length=255)
    duedate = models.DateTimeField(null=True)
    noidung = models.TextField(null=True)
    kind = models.SmallIntegerField(choices=Loai.choices)
    dinhky = models.SmallIntegerField(blank=True, null=True, choices=DinhKy.choices)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.name.__str__()

    @property
    def get_class_hell(self):
        match self.kind:
            case 1:
                return "danger"
            case 2:
                return "warning"
            case 3:
                return "success"

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
