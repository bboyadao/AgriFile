from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, DetailView, ListView, DeleteView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import BaseUpdateView

from baocao.forms import BaoCaoForm
from baocao.models import MediaFile, BaoCao
# from django.contrib.auth.mixins import PermissionRequiredMixin


class BaoCaoDetail(DetailView):
    model = BaoCao
    template_name = 'baocao/detail.html'


class BaoCaoCreate(LoginRequiredMixin, FormView):

    form_class = BaoCaoForm
    template_name = 'baocao/create.html'
    pk = None

    def get_success_url(self):
        return reverse('baocao_detail', kwargs={'pk': self.pk})

    def form_valid(self, form):
        item = form.save()
        self.pk = item.pk
        messages.success(self.request, f"Tạo báo cáo thành công.")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            baocao = form.save(commit=False)
            baocao.created_by = request.user
            baocao.save()
            a = []
            for f in files:
                print(f.__dict__)
                a.append(MediaFile(baocao=baocao,
                                   media=f,
                                   filename=f._name,
                                   filetype=f.content_type))
            MediaFile.objects.bulk_create(a)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BaoCaoList(LoginRequiredMixin, ListView):
    model = BaoCao
    template_name = "baocao/list.html"

    def get_queryset(self):
        qs = BaoCao.objects.filter(created_by=self.request.user)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(name__icontains=query)
        return qs


class BaoCaoUpdate(UpdateView):
    model = BaoCao
    form_class = BaoCaoForm
    template_name = 'baocao/update.html'

    def get_success_url(self):
        return reverse("baocao_detail", kwargs={'pk': self.get_object().pk})

    def form_valid(self, form):
        messages.success(self.request, f"Sửa báo cáo thành công.")
        return super().form_valid(form)


class BaoCaoDelete(DeleteView):
    pass


class AddNote(BaseUpdateView):
    form_class = BaoCaoForm
    template_name = 'baocao/detail.html'
    model = BaoCao

    def get_success_url(self):
        return reverse('baocao_detail', kwargs={'pk': self.get_object().pk})

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        note = request.POST.get("note", "loi roi call admin")
        obj.note = note
        obj.save()
        messages.success(self.request, f"Thêm ghi chú thành công")
        return HttpResponseRedirect(self.get_success_url())
