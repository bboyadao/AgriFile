from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from user.forms import UserForm, UserUpdateForm
from user.models import User


class ListUser(ListView):
    queryset = User.objects.all()
    model = User


class CreateUser(CreateView):
    template_name = "user/user_create.html"
    queryset = User.objects.all()
    form_class = UserForm


class DetailUser(DetailView):
    template_name = "user/user_detail.html"
    model = User
    slug_field = "username"


class UpdateUser(UpdateView):
    template_name = "user/user_update.html"
    model = User
    slug_field = "username"
    form_class = UserUpdateForm

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super().form_valid(form)
