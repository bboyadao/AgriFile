from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordContextMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView
from django.utils.translation import gettext_lazy as _


class ChangePass(PasswordContextMixin, FormView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy("password_change_done")
	template_name = "user/change_pass.html"
	title = _("Password change")

	@method_decorator(sensitive_post_parameters())
	@method_decorator(csrf_protect)
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs["user"] = self.request.user
		return kwargs

	def form_valid(self, form):
		form.save()
		# Updating the password logs out all other sessions for the user
		# except the current one.
		update_session_auth_hash(self.request, form.user)
		return super().form_valid(form)


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
	template_name = "user/password_change_done.html"
	title = _("Password change successful")

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


class Login(LoginView):
	template_name = "user/login.html"


class Zone(object):
	def __init__(self, name, child):
		self.name = name
		self.child = child


class Menu(object):
	def __init__(self, name, child, icon, open=None):
		self.name = name
		self.open = open
		self.child = child
		self.icon = icon


class Nav(object):
	def __init__(self, name, icon, link):
		self.name = name
		self.icon = icon
		self.link = link


data = [
	{
		"name": "ADMIN ZONE",
		"menu": [
			{
				"name": "Quản lý người dùng",
				"icon": "fa fa-user",
				"navs": [
					{"name": "Danh sách", "icon": "fa fa-list", "link": 'user_list'},
					{"name": "Tạo mới", "icon": "fa fa-user-plus", "link": "user_create"},

				]
			},
			{
				"name": "Cài đặt",
				"icon": "fa fa-cogs",
				"navs": [
					{"name": "Phòng ban", "icon": "fa fa-building", "link": "phongban_list"},
					{"name": "Nơi nhận", "icon": "fa fa-paper-plane", "link": "noinhan_list"},
					{"name": "Lịch báo cáo", "icon": "fa fa-calendar", "link": "lichbaocao_list"},
				],
			},
			{
				"name": "Quản lý Báo Cáo",
				"icon": "fa fa-hashtag",
				"navs": [
					{"name": "Danh Sách Báo Cáo", "icon": "fa fa-list-ol", "link": 'admin_baocao_list'},

				]
			},
		]
	},
	{
		"name": "WORK ZONE",
		"menu": [
			{
				"name": "Báo cáo",
				"icon": "fa fa-clipboard",
				"navs": [
					{"name": "Danh Sách Đã Nộp", "icon": "fa fa-list-ol", "link": "baocao_list"},
					{"name": "Tạo Mới", "icon": "fa fa-plus", "link": "baocao_create"},

				]
			},
		]
	},

]


def global_templates_context_processors(request):
	current_view = request.resolver_match.url_name
	zones = []
	for zone in data:
		menus = []
		for menu in zone["menu"]:
			open_menu = False
			navs = []
			for nav in menu["navs"]:
				###################
				if current_view == nav["link"]:
					open_menu = True
				###################
				n = Nav(name=nav["name"], icon=nav["icon"], link=nav["link"])
				navs.append(n)
			m = Menu(menu["name"], child=navs, icon=menu["icon"], open=open_menu)
			menus.append(m)

		z = Zone(name=zone["name"], child=menus)
		zones.append(z)

	return {"ZONES": zones, "current_view": current_view}
