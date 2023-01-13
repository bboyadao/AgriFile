import django
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm, NumberInput
from django.utils.functional import lazy

from user.models import User
from setmeup.models import PhongBan


def getchoice():
	try:
		return PhongBan.objects.all()
	except django.db.utils.OperationalError:
		return []


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
		fields = ["username", "full_name", "phongban"]
		error_messages = {
			NON_FIELD_ERRORS: {
				'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}
		PB = PhongBan.objects.all()
		widgets = {
			'username': NumberInput(),
			'phongban':  forms.Select(choices=PB)
			# 'phongban':  forms.(choices=lazy(PhongBan.objects.all()))
		}
		labels = {
			'username': "Số điện thoại",
			"full_name": "Tên",
			"phongban": "Phòng ban"
		}
		help_texts = {
			'username': 'Sđt (09xxx)',
		}


class UserUpdateForm(ModelForm):

	class Meta:
		model = User
		fields = ["full_name", "phongban"]
		error_messages = {
			NON_FIELD_ERRORS: {
				'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
			}
		}

		widgets = {
			'username': NumberInput(),
			'phongban':  forms.Select(choices=PhongBan.objects.all())
		}
		labels = {
			'username': "Số điện thoại",
			"full_name": "Tên",
			"phongban": "Phòng ban"
		}
		help_texts = {
			'username': 'Sđt (09xxx)',
		}