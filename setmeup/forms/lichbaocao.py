from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from setmeup.models import LichBaoCao


class DateTimePickerInput(forms.DateTimeInput):
	input_type = 'datetime'


class LichBaoCaoForm(ModelForm):
	duedate = forms.DateTimeField(
		label="Hạn nộp",
		input_formats=['%d/%m/%Y %H:%M'],
		widget=forms.TextInput(
			attrs={
				'class': 'datetimepicker',
				"autocomplete": "off"
			}
		))

	class Meta:
		model = LichBaoCao
		fields = ["kind", "dinhky", "name", "duedate", "noidung", ]
		widgets = {
			'name': forms.TextInput(),
			'dinhky': forms.Select(choices=LichBaoCao.DinhKy.choices)
		}

		labels = {
			'name': "Tên",
			"duedate": "Hạn nộp",
			"noidung": "Nội dung",
			"kind": "Loại",
			"dinhky": "Định kỳ"
		}

	def clean(self):
		cleaned_data = super().clean()
		kind = cleaned_data.get("kind", None)
		dinhky = cleaned_data.get("dinhky", None)

		if kind == LichBaoCao.Loai.dinhky and not dinhky:
			raise ValidationError(
				"Sai loại"
			)

		if all([kind, dinhky]):
			if kind not in LichBaoCao.Loai.values or dinhky not in LichBaoCao.DinhKy.values:
				raise ValidationError(
					"lien he admin"
				)
