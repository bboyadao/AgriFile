from django import forms
from django_select2.forms import HeavySelect2Mixin, Select2Widget, ModelSelect2Widget

from baocao.models import BaoCao, ThongKe


def get_thang():
	t = []
	for i in range(1, 13):
		t.append((i, f"Tháng {i}"))
	return t


def get_quy():
	q = []
	for i in range(1, 5):
		q.append((i, f"Quý {i}"))
	return q


def get_nam():
	n = []
	for i in range(2023, 2043):
		n.append((i, f"Năm {i}"))
	return n


class ThongkeForm(forms.ModelForm):
	class Meta:
		model = ThongKe
		fields = '__all__'
		widgets = {
			'country': ModelSelect2Widget(
				model=ThongKe,
				search_fields=['name__icontains'],
			),
			'city': ModelSelect2Widget(
				model=ThongKe,
				search_fields=['name__icontains'],
				dependent_fields={'country': 'country'},
				max_results=500,
			)
		}
