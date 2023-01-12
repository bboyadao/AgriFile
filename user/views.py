from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordContextMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import ListView, CreateView, DetailView, UpdateView, FormView

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


class ChangePassUser(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "user/change_pass.html"
    title = "Password change"

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