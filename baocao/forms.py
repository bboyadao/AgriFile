from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from baocao.models import BaoCao


class BaoCaoForm(forms.ModelForm):
	file_field = forms.FileField(label="Files",
		widget=forms.ClearableFileInput(
			attrs={
				'multiple': True,
			}),
	)
	thoigian = forms.SplitDateTimeField(label="Thời gian",
		widget=AdminSplitDateTime())

	class Meta:
		model = BaoCao
		fields = [
			"name", "noidung",
			"nguoi_duyet", "nguoi_ky",
			"phongban", "noinhan",
			"thoigian",
			"file_field"
		]

		labels = {
			'file_field': "File đính kèm",
			"noidung": "Nội dung",
			"nguoi_duyet": "Người duyệt",
			"nguoi_ky": "Người Ký",
			"phongban": "Phòng ban",
			"noinhan": "Nơi nhận"
		}
