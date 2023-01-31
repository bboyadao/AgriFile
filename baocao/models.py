import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


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


class ThongKe(MPTTModel):
	class ThongkeKind(models.IntegerChoices):
		thang = 1, "Tháng"
		quy = 2, "Quý"
		nam = 3, "Năm"

	name = models.CharField(max_length=255, unique=True)
	kind = models.SmallIntegerField(choices=ThongkeKind.choices)
	val = models.SmallIntegerField()
	created_at = models.DateTimeField(auto_created=True, null=True)
	baocao = models.ManyToManyField("baocao.BaoCao")
	nam = models.SmallIntegerField(null=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	count = models.IntegerField(default=0)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return f"{self.name}"

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
		parent = None
		print(list(reversed(ThongKe.ThongkeKind.choices)))
		for kind, _name in reversed(ThongKe.ThongkeKind.choices):
			val = ThongKe.my_val_by_kind(dt=ins.thoigian, kind=kind)
			name = f"{_name} {val}"

			if kind != ThongKe.ThongkeKind.nam:
				name += f" Năm {ins.thoigian.year}"
			try:
				t = ThongKe.objects.get(name=name, kind=kind, val=val, parent=parent, nam=ins.thoigian.year)
			except ThongKe.DoesNotExist as e:
				t = ThongKe.objects.create(
					name=name,
					kind=kind,
					val=val,
					parent=parent,
					nam=ins.thoigian.year,
				)

			t.count += 1
			t.save()
			parent = t
	# t.baocao.add(ins)


@receiver(post_save, sender=BaoCao)
def update_thongke(sender, instance, created, **kwargs):  # noqa
	if created:
		ThongKe.get_or_new(instance)
