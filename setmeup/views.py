import calendar
from datetime import datetime, date, timedelta
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import PasswordContextMixin
from django.db.models import Count, Value, Q
from django.db.models.functions import ExtractYear
from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django_filters.views import FilterView

from baocao.models import BaoCao, ThongKe
from setmeup.filter import BaoCaoFilterset
from setmeup.forms.lichbaocao import LichBaoCaoForm
from setmeup.models import NoiNhan, PhongBan, LichBaoCao
from user.forms import UserUpdateForm, UserForm
from user.models import User
from django.views.generic.edit import FormView
from io import BytesIO

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


class CreateUser(LoginRequiredMixin, CreateView):
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
            messages.success(self.request, f"Tạo thành công: <strong>{user.username} | {password}</strong>")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DetailUser(LoginRequiredMixin, DetailView):
    template_name = "user/user_detail.html"
    model = User


class ResetPass(LoginRequiredMixin, UpdateView):
    template_name = "user/user_list.html"
    model = User
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


class UpdateUser(LoginRequiredMixin, UpdateView):
    template_name = "user/user_update.html"
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        messages.success(self.request, "Cập nhật thông tin thành công.")
        return super().form_valid(form)


class ChangePassUser(LoginRequiredMixin, PasswordContextMixin, FormView):
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


class DeleteUser(LoginRequiredMixin, DeleteView):
    template_name = "user/user_confirm_delete.html"
    model = User
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        messages.success(self.request, f"Xóa người dùng thành công.")
        return super().form_valid(form)


class NoiNhanList(LoginRequiredMixin, ListView):
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


class NoiNhanDetail(LoginRequiredMixin, DetailView):
    model = NoiNhan


class NoiNhanCreate(LoginRequiredMixin, CreateView):
    template_name = "noinhan/create.html"
    queryset = NoiNhan.objects.all()
    fields = ["name"]
    success_url = reverse_lazy("noinhan_list")


class NoiNhanUpdate(LoginRequiredMixin, UpdateView):
    template_name = "noinhan/update.html"
    model = NoiNhan
    fields = ["name"]
    success_url = reverse_lazy("noinhan_list")

    def form_valid(self, form):
        messages.success(self.request, f"Sửa nơi nhận thành công.")
        return super().form_valid(form)


class NoiNhanDelete(LoginRequiredMixin, DeleteView):
    model = NoiNhan
    success_url = reverse_lazy('noinhan_list')
    template_name = 'noinhan/delete.html'

    def form_valid(self, form):
        messages.error(self.request, f"Xóa nơi nhận thành công.")
        return super().form_valid(form)


class PhongBanList(LoginRequiredMixin, ListView):
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


class PhongBanDetail(LoginRequiredMixin, DetailView):
    model = PhongBan


class PhongBanCreate(LoginRequiredMixin, CreateView):
    template_name = "phongban/create.html"
    queryset = PhongBan.objects.all()
    fields = ["name"]
    success_url = reverse_lazy("phongban_list")


class PhongBanUpdate(LoginRequiredMixin, UpdateView):
    template_name = "phongban/update.html"
    model = PhongBan
    fields = ["name"]
    success_url = reverse_lazy("phongban_list")

    def form_valid(self, form):
        messages.success(self.request, f"Sửa nơi nhận thành công.")
        return super().form_valid(form)


class PhongBanDelete(LoginRequiredMixin, DeleteView):
    model = PhongBan
    success_url = reverse_lazy('phongban_list')
    template_name = 'phongban/delete.html'

    def form_valid(self, form):
        messages.error(self.request, f"Xóa phòng ban thành công.")
        return super().form_valid(form)


class LichBaoCaoList(LoginRequiredMixin, ListView):
    template_name = "lichbaocao/list.html"
    queryset = LichBaoCao.objects.all()
    model = LichBaoCao
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            return qs.filter(name__icontains=query)
        return qs


class LichBaoCaoDetail(LoginRequiredMixin, DetailView):
    model = LichBaoCao


class LichBaoCaoCreate(LoginRequiredMixin, CreateView):
    template_name = "lichbaocao/create.html"
    queryset = LichBaoCao.objects.all()
    success_url = reverse_lazy("lichbaocao_list")
    form_class = LichBaoCaoForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class LichBaoCaoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "lichbaocao/update.html"
    model = LichBaoCao
    success_url = reverse_lazy("lichbaocao_list")
    form_class = LichBaoCaoForm

    def form_valid(self, form):
        messages.success(self.request, f"Sửa lịch báo cáo thành công")
        return super().form_valid(form)


class LichBaoCaoDelete(LoginRequiredMixin, DeleteView):
    model = LichBaoCao
    success_url = reverse_lazy('lichbaocao_list')
    template_name = 'lichbaocao/delete.html'

    def form_valid(self, form):
        messages.error(self.request, f"Xóa lịch báo cáo thành công.")
        return super().form_valid(form)


class AdminBaoCao(LoginRequiredMixin, FilterView):
    model = BaoCao
    template_name = "baocao/admin_baocao_list.html"
    filterset_class = BaoCaoFilterset
    paginate_by = 5
    filter = None


class ThongKeView(ListView):
    model = ThongKe
    template_name = "thongke/list.html"

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related("baocao")\
            .annotate(total=Count('baocao'))
        return qs


def get_start_date(quarter, year):
    match quarter:
        case 1:
            return date(year=year, month=1, day=1)
        case 2:
            return date(year=year, month=4, day=1)
        case 3:
            return date(year=year, month=7, day=1)
        case 4:
            return date(year=year, month=10, day=1)


class ThongKeDetailView(DetailView):
    model = ThongKe
    template_name = "thongke/detail.html"

    def map_shit(self):
        obj = self.get_object()
        match obj.kind:
            case ThongKe.ThongkeKind.quy:
                year = obj.nam
                days = 366 if calendar.isleap(year) else 365
                start = get_start_date(obj.val, obj.nam)
                end = start + timedelta(3 * days / 12)
                return start, end

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        qs = BaoCao.objects.filter(thoigian__year=obj.nam)
        q = Q()
        match obj.kind:
            case ThongKe.ThongkeKind.quy:
                start, end = self.map_shit()
                q = Q(thoigian__range=[start, end])
            case ThongKe.ThongkeKind.nam:
                q = Q(thoigian__year=obj.val)
            case ThongKe.ThongkeKind.thang:
                q = Q(thoigian__month=obj.val)

        context['baocao_list'] = qs.filter(q)
        context['phongban'] = qs.values("phongban__name").annotate(phongban_count=Count('phongban__name'))
        context['noinhan'] = qs.values("noinhan__name").annotate(noinhan_count=Count('noinhan__name'))

        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        download = request.GET.get("download")
        if download == '1':
            context = self.get_context_data()
            qs = context['baocao_list']
            excel_file = BaoCao.thongke.gen_file_thongke(qs)
            excel_file.seek(0)
            response = StreamingHttpResponse(excel_file,
                                             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename=Thống kê {self.object.name}.xlsx'.encode('utf-8')
            return response
        return self.render_to_response(context)


class NoTif(ListView):
    template_name = "lichbaocao/notif.html"
    model = LichBaoCao
    ordering = "duedate"

    def get_queryset(self):
        qs = super().get_queryset().filter(
            duedate__range=(
                timezone.now().date(),
                timezone.now() + timedelta(days=30)
            )
        )
        return qs


