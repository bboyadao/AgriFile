import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone


class ThongKeManager(models.Manager):
	pass


class BaoCaoManager(models.Manager):
	pass


class BaoCao(models.Model):
	name = models.CharField(max_length=255)
	noidung = models.TextField()
	nguoi_duyet = models.ForeignKey(
		"user.User", on_delete=models.SET_NULL, null=True, related_name="nguoi_duyet")
	nguoi_ky = models.ForeignKey(
		"user.User", on_delete=models.SET_NULL, null=True, related_name="nguoi_ky")
	nguoi_soan = models.ForeignKey(
		"user.User", on_delete=models.SET_NULL, null=True, related_name="nguoi_soan")
	phongban = models.ForeignKey(
		"setmeup.PhongBan", on_delete=models.SET_NULL, null=True)
	noinhan = models.ForeignKey(
		"setmeup.NoiNhan", on_delete=models.SET_NULL, null=True)
	note = models.TextField()
	thoigian = models.DateTimeField()
	created_by = models.ForeignKey(
		"user.User", on_delete=models.PROTECT)

	nof = models.ForeignKey("setmeup.LichBaoCao", on_delete=models.SET_NULL, null=True)
	created_at = models.DateTimeField(auto_now=True)
	thongke = ThongKeManager()
	objects = BaoCaoManager()

	class Meta:
		ordering = ["-pk"]

	@property
	def get_absolute_url(self):
		return reverse('baocao_detail', args=[self.pk.__str__()])


def media_directory_path(instance, filename):
	return os.path.join(
		'baocao',
		f'{instance.baocao.pk}',
		f'{timezone.now().timestamp().__str__()}_{filename}')


class MediaFile(models.Model):
	baocao = models.ForeignKey("baocao.BaoCao", on_delete=models.CASCADE)
	media = models.FileField(upload_to=media_directory_path)
	filename = models.CharField(max_length=255, null=True)
	filetype = models.CharField(max_length=255, null=True)


class ThongKe(models.Model):
	class ThongkeKind(models.IntegerChoices):
		thang = 1, "Tháng"
		quy = 2, "Quý"
		nam = 3, "Năm"

	kind = models.SmallIntegerField(choices=ThongkeKind.choices)
	val = models.SmallIntegerField()
	year = models.SmallIntegerField()
	baocao = models.ManyToManyField("baocao.BaoCao")

	def __str__(self):
		return f"{self.get_kind_display()} {self.val} {self.year}"

	@staticmethod
	def get_quarter(dt):
		return (dt.month - 1) // 3 + 1

	@staticmethod
	def my_val_by_kind(kind, dt):
		match kind:
			case ThongKe.ThongkeKind.thang:
				return dt.month
			case ThongKe.ThongkeKind.quy:
				return ThongKe.get_quarter(dt)
			case ThongKe.ThongkeKind.nam:
				return dt.year

	@classmethod
	def get_or_new(cls, ins):
		for kind in ThongKe.ThongkeKind.values:
			val = ThongKe.my_val_by_kind(kind=kind, dt=ins.thoigian)
			t, _ = ThongKe.objects.get_or_create(
				kind=kind, val=val, year=ins.thoigian.year
			)
			t.baocao.add(ins)


@receiver(post_save, sender=BaoCao, dispatch_uid="update_to_report")
def update_thongke(sender, instance, **kwargs):  # noqa
	ThongKe.get_or_new(instance)