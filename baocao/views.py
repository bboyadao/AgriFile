from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, DetailView, ListView, DeleteView, UpdateView

from baocao.forms import BaoCaoForm
from baocao.models import MediaFile, BaoCao


class BaoCaoDetail(DetailView):
    model = BaoCao
    template_name = 'baocao/detail.html'


class BaoCaoCreate(FormView):
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
            baocao = form.save()
            a = []
            for f in files:
                a.append(MediaFile(baocao=baocao, media=f))
            MediaFile.objects.bulk_create(a)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BaoCaoList(ListView):
    model = BaoCao
    template_name = "baocao/list.html"
    # update qs


class BaoCaoUpdate(UpdateView):
    pass


class BaoCaoDelete(DeleteView):
    pass
