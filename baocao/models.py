import os

from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone


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
		"user.User", on_delete=models.SET_NULL, null=True)

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


# @receiver(post_save, sender=BaoCao, dispatch_uid="update_to_report")
# def update_stock(sender, instance, **kwargs):
#     instance.product.stock -= instance.amount
#     instance.product.save()