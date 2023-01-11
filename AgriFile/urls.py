from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from AgriFile.views import Login


def index(request):
	context = {}
	return render(request, 'adminlte/index.html', context)


urlpatterns = [
	path('', index),
	path('login/', Login.as_view()),
	path('admin/', admin.site.urls),
	path('user/', include("user.urls")),
	path('file/', include("file.urls")),
]
