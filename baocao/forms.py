from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

from baocao.models import BaoCao


class BaoCaoForm(forms.ModelForm):
	file_field = forms.FileField(
		widget=forms.ClearableFileInput(
			attrs={
				'multiple': True,
			}),
	)
	thoigian = forms.SplitDateTimeField(widget=AdminSplitDateTime())

	class Meta:
		model = BaoCao
		fields = '__all__'
