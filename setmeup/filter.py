import django_filters
from django_filters.widgets import DateRangeWidget

from baocao.models import BaoCao


class BaoCaoFilterset(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains', label="Tên có chứa")

	thoigian = django_filters.DateTimeFromToRangeFilter(
		widget=DateRangeWidget(
			attrs={
				'class': 'row datetimepicker form-control',
				"autocomplete": "off",

			}
		))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.filters['created_by'].label = "Người tạo"
		self.filters['nguoi_soan'].label = "Người soạn"
		self.filters['nguoi_ky'].label = "Người ký"
		self.filters['nguoi_duyet'].label = "Người duyệt"
		self.filters['noidung'].label = "Nội dung có chứa"
		self.filters['phongban'].label = "Phòng ban"
		self.filters['noinhan'].label = "Nơi nhận "
		self.filters['thoigian'].label = "Thời gian"
		self.filters['name'].label = "Tên"

	class Meta:
		model = BaoCao
		fields = [
			"created_by",
			"nguoi_soan",
			"nguoi_duyet",
			"nguoi_ky",
			"name",

			"noidung",
			"phongban",
			"noinhan",
			"thoigian",
		]

