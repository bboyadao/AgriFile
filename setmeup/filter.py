
import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from django import forms
from django.forms import DateInput, DateTimeInput
from django_filters.widgets import DateRangeWidget

from baocao.models import BaoCao


class BaoCaoFormFilter(forms.ModelForm):
    class Meta:
        model = BaoCao
        fields = [
            "created_by",
            "phongban",
            "noinhan",
            "thoigian"
        ]

        labels = {
            "created_by": "Nộp bởi"
        }

    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Div('created_by', css_class='span6'),
            Div('phongban', css_class='span6'),
            css_class='row-fluid'),
    )


class BaoCaoFilterset(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Tên có chứa")
    thoigian = django_filters.DateTimeFromToRangeFilter(widget=DateRangeWidget(
        attrs={
            'class': 'datetimepicker',
            "autocomplete": "off"
        }
        ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['created_by'].label = "Người tạo"
        self.filters['phongban'].label = "Phòng ban"
        self.filters['noinhan'].label = "Nơi nhận "
        self.filters['thoigian'].label = "Thời gian"

    class Meta:
        model = BaoCao
        fields = [
            "created_by",
            "phongban",
            "noinhan",
            "thoigian"
        ]