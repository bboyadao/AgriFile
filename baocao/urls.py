from django.urls import path
from baocao.views import BaoCaoCreate, BaoCaoDetail, BaoCaoList, BaoCaoUpdate, BaoCaoDelete

urlpatterns = [
	path('', BaoCaoList.as_view(), name="baocao_list"),
	path('create/', BaoCaoCreate.as_view(), name="baocao_create"),
	path('<int:pk>/', BaoCaoDetail.as_view(), name="baocao_detail"),
	path('<int:pk>/update/', BaoCaoUpdate.as_view(), name="baocao_update"),
	path('<int:pk>/delete/', BaoCaoDelete.as_view(), name="baocao_delete"),

]
