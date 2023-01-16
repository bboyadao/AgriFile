import datetime
import sys

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import PasswordContextMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView

from baocao.models import BaoCao
from setmeup.filter import BaoCaoFilterset
from setmeup.forms.lichbaocao import LichBaoCaoForm
from setmeup.models import NoiNhan, PhongBan, LichBaoCao
from user.forms import UserUpdateForm, UserForm
from user.models import User
from django.views.generic.edit import FormView
# if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:


class ListUser(PermissionRequiredMixin, ListView):
    permission_required = 'view_user'
    queryset = User.objects.all()
    model = User
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            return qs.filter(full_name__icontains=query)
        return qs


class CreateUser(CreateView):
    model = User
    template_name = "user/user_create.html"
    queryset = User.objects.all()
    form_class = UserForm
    success_url = reverse_lazy("user_list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save(commit=False)
            import secrets
            import string
            alphabet = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(alphabet) for i in range(20))
            user.set_password(password)
            user.save()
            messages.success(self.request, f"Tạo thành công: <strong>{user.username} | {password}</strong>`")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DetailUser(DetailView):
    template_name = "user/user_detail.html"
    model = User
    slug_field = "username"


class ResetPass(UpdateView):
    template_name = "user/user_list.html"
    model = User
    slug_field = "username"
    fields = []

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        import secrets
        import string
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        obj.set_password(password)
        obj.save()
        messages.success(self.request, f"Reset password thành công: <strong>{obj.username} | {password}</strong>")
        return HttpResponseRedirect(reverse_lazy("user_list"))


class UpdateUser(UpdateView):
    template_name = "user/user_update.html"
    model = User
    slug_field = "username"
    form_class = UserUpdateForm

    def form_valid(self, form):
        messages.success(self.request, "Cập nhật thông tin thành công.")
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


class DeleteUser(DeleteView):
    template_name = "user/user_confirm_delete.html"
    model = User
    slug_field = "username"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        messages.success(self.request, f"Xóa người dùng thành công.")
        return super().form_valid(form)


class NoiNhanList(ListView):
    template_name = "noinhan/list.html"
    queryset = NoiNhan.objects.all()
    model = NoiNhan
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            return qs.filter(name__icontains=query)
        return qs


class NoiNhanDetail(DetailView):
    model = NoiNhan


class NoiNhanCreate(CreateView):
    template_name = "noinhan/create.html"
    queryset = NoiNhan.objects.all()
    fields = ["name"]
    success_url = reverse_lazy("noinhan_list")


class NoiNhanUpdate(UpdateView):
    template_name = "noinhan/update.html"
    model = NoiNhan
    fields = ["name"]
    success_url = reverse_lazy("noinhan_list")

    def form_valid(self, form):
        messages.success(self.request, f"Sửa nơi nhận thành công.")
        return super().form_valid(form)


class NoiNhanDelete(DeleteView):
    model = NoiNhan
    success_url = reverse_lazy('noinhan_list')
    template_name = 'noinhan/delete.html'

    def form_valid(self, form):
        messages.error(self.request, f"Xóa nơi nhận thành công.")
        return super().form_valid(form)


class PhongBanList(ListView):
    template_name = "phongban/list.html"
    queryset = PhongBan.objects.all()
    model = PhongBan
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            return qs.filter(name__icontains=query)
        return qs


class PhongBanDetail(DetailView):
    model = PhongBan


class PhongBanCreate(CreateView):
    template_name = "phongban/create.html"
    queryset = PhongBan.objects.all()
    fields = ["name"]
    success_url = reverse_lazy("phongban_list")


class PhongBanUpdate(UpdateView):
    template_name = "phongban/update.html"
    model = PhongBan
    fields = ["name"]
    success_url = reverse_lazy("phongban_list")

    def form_valid(self, form):
        messages.success(self.request, f"Sửa nơi nhận thành công.")
        return super().form_valid(form)


class PhongBanDelete(DeleteView):
    model = PhongBan
    success_url = reverse_lazy('phongban_list')
    template_name = 'phongban/delete.html'

    def form_valid(self, form):
        messages.error(self.request, f"Xóa phòng ban thành công.")
        return super().form_valid(form)


class LichBaoCaoList(ListView):
    template_name = "lichbaocao/list.html"
    queryset = LichBaoCao.objects.all()
    model = LichBaoCao
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            return qs.filter(name__icontains=query)
        return qs


class LichBaoCaoDetail(DetailView):
    model = LichBaoCao


class LichBaoCaoCreate(CreateView):
    template_name = "lichbaocao/create.html"
    queryset = LichBaoCao.objects.all()
    success_url = reverse_lazy("lichbaocao_list")
    form_class = LichBaoCaoForm


class LichBaoCaoUpdate(UpdateView):
    template_name = "lichbaocao/update.html"
    model = LichBaoCao
    success_url = reverse_lazy("lichbaocao_list")
    form_class = LichBaoCaoForm

    def form_valid(self, form):
        messages.success(self.request, f"Sửa lịch báo cáo thành công")
        return super().form_valid(form)


class LichBaoCaoDelete(DeleteView):
    model = LichBaoCao
    success_url = reverse_lazy('lichbaocao_list')
    template_name = 'lichbaocao/delete.html'

    def form_valid(self, form):
        messages.error(self.request, f"Xóa lịch báo cáo thành công.")
        return super().form_valid(form)


class AdminBaoCao(FilterView):
    model = BaoCao
    template_name = "baocao/admin_baocao_list.html"
    filterset_class = BaoCaoFilterset
    paginate_by = 5
    filter = None


class NoTif(ListView):
    template_name = "lichbaocao/notif.html"
    model = LichBaoCao
    ordering = "duedate"

    def get_queryset(self):
        qs = super().get_queryset().filter(
            duedate__range=(
                timezone.now().date(),
                timezone.now() + datetime.timedelta(days=30)
            )
        )
        print(qs.query)
        return qs
