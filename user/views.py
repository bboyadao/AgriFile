from django.shortcuts import render
from django.views.generic import ListView
from user.models import User


class ListUser(ListView):
    model = User



def create_user(request):
    return render(request, "user/user_create.html", {})
