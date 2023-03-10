import datetime

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordContextMixin, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView
from django.utils.translation import gettext_lazy as _

from setmeup.models import LichBaoCao


class ChangePass(LoginRequiredMixin, PasswordContextMixin, FormView):
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


class PasswordChangeDoneView(LoginRequiredMixin, PasswordContextMixin, TemplateView):
	template_name = "user/password_change_done.html"
	title = _("Password change successful")

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


class Logout(LogoutView):
	template_name = "user/logged_out.html"


class Login(LoginView):
	template_name = "user/login.html"

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("index"))
		return super().get(request, *args, **kwargs)


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
		"name": "ADMIN",
		"menu": [
			{
				"name": "Qu???n l?? ng?????i d??ng",
				"icon": "fa fa-user",
				"navs": [
					{"name": "Danh s??ch", "icon": "fa fa-list", "link": 'user_list'},
					{"name": "T???o m???i", "icon": "fa fa-user-plus", "link": "user_create"},

				]
			},

			{
				"name": "Qu???n l?? B??o C??o",
				"icon": "fa fa-hashtag",
				"navs": [
					{"name": "Danh S??ch B??o C??o", "icon": "fa fa-list-ol", "link": 'admin_baocao_list'},

				]
			},
			{
				"name": "Th???ng k??",
				"icon": "far fa-chart-bar",
				"navs": [
					{"name": "Danh s??ch", "icon": "fa fa-calendar", "link": 'thongke'},
					# {"name": "Qu??", "icon": "far fa-calendar-alt", "link": 'admin_baocao_list'},
					# {"name": "N??m", "icon": "far fa-calendar", "link": 'admin_baocao_list'},
				]
			}
		]
	},
	{
		"name": "USER",
		"menu": [
{
				"name": "C??i ?????t",
				"icon": "fa fa-cogs",
				"navs": [
					{"name": "Ph??ng ban", "icon": "fa fa-building", "link": "phongban_list"},
					{"name": "N??i nh???n", "icon": "fa fa-paper-plane", "link": "noinhan_list"},
					{"name": "L???ch b??o c??o", "icon": "fa fa-calendar", "link": "lichbaocao_list"},
				],
			},
			{
				"name": "B??o c??o",
				"icon": "fa fa-clipboard",
				"navs": [
					{"name": "Danh S??ch ???? N???p", "icon": "fa fa-list-ol", "link": "baocao_list"},
					{"name": "T???o M???i", "icon": "fa fa-plus", "link": "baocao_create"},

				]
			},
		]
	},

]


def global_templates_context_processors(request):
	current_view = request.resolver_match.url_name
	zones = []
	user_zone = []
	admin_zone = []
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
		if z.name == "ADMIN":
			admin_zone.append(z)
		elif z.name == "USER":
			user_zone.append(z)
		zones.append(z)

	num_of_nof = LichBaoCao.objects.filter(
		duedate__range=(
			timezone.now().date(),
			timezone.now() + datetime.timedelta(days=7)
		)
	).count()
	g_data = {
		"current_view": current_view,
		"num_of_nof": num_of_nof
	}

	if request.user.is_superuser:
		g_data.update(ZONES=zones)
	else:
		g_data.update(ZONES=user_zone)

	return g_data
