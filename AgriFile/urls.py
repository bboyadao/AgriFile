from django.shortcuts import render
from django.urls import path, include
from AgriFile.views import Login, ChangePass, PasswordChangeDoneView, Logout
from django.views.i18n import JavaScriptCatalog

from setmeup.views import AdminBaoCao


def index(request):
	context = {}
	return render(request, 'adminlte/index.html', context)


urlpatterns = [
	path('', index, name="index"),
	path('login/', Login.as_view(), name="login"),
	path('logout/', Logout.as_view(), name="logout"),

	path('change_pass/', ChangePass.as_view(), name="change_pass"),
	path(
			"password_change/done/",
			PasswordChangeDoneView.as_view(),
			name="password_change_done",
		),

	# path('admin/', admin.site.urls),
	path('user/', include("user.urls")),
	path('setup/', include("setmeup.urls")),
	path('baocao/', include("baocao.urls")),
	path('jsi18n/', JavaScriptCatalog.as_view(), name='js-catlog'),

	# Admin Bao Cao
	path('admin/baocao/', AdminBaoCao.as_view(), name="admin_baocao_list"),

]
