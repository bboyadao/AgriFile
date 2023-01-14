
import django_filters

from baocao.models import BaoCao


class BaoCaoFilterset(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = BaoCao
        fields = [
            "phongban",
            "noinhan"
        ]