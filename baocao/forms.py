from django import forms

from baocao.models import BaoCao


class BaoCaoQuickForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		icons = getattr(self.Meta, 'icons', dict())
		for field_name, field in self.fields.items():
			print(field_name, field)
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
			"nof",
			"name",
			"noidung",
			"nguoi_soan",
			"nguoi_duyet",
			"nguoi_ky",
			"phongban",
			"noinhan",
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


class BaoCaoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		nof = kwargs.pop('nof', None)
		if nof:
			self.base_fields['nof'].initial = nof

		super().__init__(*args, **kwargs)
		icons = getattr(self.Meta, 'icons', dict())
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'
			if field_name == "nof":
				field.widget.attrs["disabled"] = True
				field.widget.attrs["class"] = "form-control form-control select2bs4 select2-hidden-accessible"

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
			"nof",
			"name",
			"noidung",
			"nguoi_soan",
			"nguoi_duyet",
			"nguoi_ky",
			"phongban",
			"noinhan",
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