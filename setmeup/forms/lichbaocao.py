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
	duedate = forms.SplitDateTimeField(widget=AdminSplitDateTime())

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
		# fields = ["name", "duedate"]
		fields = "__all__"

		widgets = {
			'name': forms.TextInput(),
			# "duedate": AdminSplitDateTime()
		}
		# error_messages = {
		# 	NON_FIELD_ERRORS: {
		# 		'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
		# 	}
		# }
		#
		#
		# labels = {
		# 	'name': "Tên",
		# 	"duedate": "Ngày",
		# }
		# help_texts = {
		# 	'duedate': 'Click để chọn',
		# }
