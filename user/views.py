from django.views.generic import ListView
from user.models import User


class ListUser(ListView):
    model = User
