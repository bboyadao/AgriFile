from django import forms

from baocao.models import BaoCao


class BaoCaoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		icons = getattr(self.Meta, 'icons', dict())
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'
			if field_name in icons:
				field.icon = icons[field_name]

	file_field = forms.FileField(
		required=False, label="File đính kèm",
		widget=forms.ClearableFileInput(
			attrs={
				'multiple': True,
			}),
	)
	thoigian = forms.DateTimeField(
		label="Thời gian",
		input_formats=['%d/%m/%Y %H:%M'],
		widget=forms.TextInput(
			attrs={
				'class': 'datetimepicker',
				"autocomplete": "off"
			}
		))

	class Meta:
		model = BaoCao
		fields = [
			"name", "noidung",
			"nguoi_duyet", "nguoi_ky",
			"phongban", "noinhan",
			"nguoi_soan",
			"thoigian",
			"file_field"
		]

		labels = {
			'file_field': "File đính kèm",
			"noidung": "Nội dung",
			"nguoi_duyet": "Người duyệt",
			"nguoi_ky": "Người Ký",
			"phongban": "Phòng ban",
			"noinhan": "Nơi nhận",
			"thoigian": "Thời gian",
			"nguoi_soan": "Người soạn"
		}
		icons = {
			"thoigian": "far fa-clock"
		}