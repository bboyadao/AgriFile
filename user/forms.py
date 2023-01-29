from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm, NumberInput
from user.models import User


class UserForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-creat_user'
		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'post'
		self.helper.form_action = 'user_create'
		self.helper.add_input(Submit('submit', 'Tạo'))
		self.helper.layout = Layout(
			Field('username', "phongban"),
		)

	class Meta:
		model = User
		fields = ["username", "full_name", "title", "phongban"]
		error_messages = {
			NON_FIELD_ERRORS: {
				'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}

		widgets = {
			'username': NumberInput(),
		}
		labels = {
			'username': "Số điện thoại",
			"full_name": "Tên đầy đủ",
			"phongban": "Phòng ban",
			"title": "Chức danh"
		}
		help_texts = {
			'username': 'Sđt (09xxx)',
		}


class UserUpdateForm(ModelForm):
	username = forms.NumberInput()

	class Meta:
		model = User
		fields = ["username", "full_name", "title", "phongban"]
		error_messages = {
			NON_FIELD_ERRORS: {
				'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}

		widgets = {
			'username': NumberInput(),
		}
		labels = {
			'username': "Số điện thoại",
			"full_name": "Tên đầy đủ",
			"phongban": "Phòng ban",
			"title": "Chức danh"
		}
		help_texts = {
			'username': 'Sđt (09xxx)',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
		self.helper.form_method = 'POST'
