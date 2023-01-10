from django.contrib.auth.views import LoginView
from django.shortcuts import render


class Login(LoginView):
    template_name = "user/login.html"


def index(request):
    context = {}
    return render(request, 'adminlte/index.html', context)