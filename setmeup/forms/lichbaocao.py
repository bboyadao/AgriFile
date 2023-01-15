from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import Form, ModelForm, DateField, widgets, SplitDateTimeWidget
from setmeup.models import LichBaoCao
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class DateTimePickerInput(forms.DateTimeInput):
	input_type = 'datetime'


class LichBaoCaoForm(ModelForm):
	duedate = forms.DateTimeField(
		input_formats=['%d/%m/%Y %H:%M'],
		widget=forms.TextInput(
			attrs={
				'class': 'datetimepicker',
				"autocomplete": "off"
			}
		))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-creat_user'
		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'post'
		self.helper.form_action = 'lichbaocao_create'
		self.helper.add_input(Submit('submit', 'Tạo'))
		self.helper.layout = Layout(
			Field('name', "duedate"),
		)

	class Meta:
		model = LichBaoCao
		fields = ["name", "duedate"]
		widgets = {
			'name': forms.TextInput(),
		}

		labels = {
			'name': "Tên",
			"duedate": "Hạn nộp ",
		}
