from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from AgriFile.views import Login
from django.views.i18n import JavaScriptCatalog


def index(request):
	context = {}
	return render(request, 'adminlte/index.html', context)


urlpatterns = [
	path('', index, name="index"),
	path('login/', Login.as_view()),
	path('admin/', admin.site.urls),
	path('user/', include("user.urls")),
	path('setup/', include("setmeup.urls")),
	path('baocao/', include("baocao.urls")),
	path('jsi18n/', JavaScriptCatalog.as_view(), name='js-catlog'),

]
