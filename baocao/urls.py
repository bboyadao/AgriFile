from django.urls import path
from baocao.views import BaoCaoCreateByNof, BaoCaoDetail, BaoCaoList, BaoCaoUpdate, BaoCaoDelete, AddNote

urlpatterns = [
	path('', BaoCaoList.as_view(), name="baocao_list"),
	path('create/', BaoCaoCreateByNof.as_view(), name="baocao_create"),

	path('<pk>/', BaoCaoDetail.as_view(), name="baocao_detail"),
	path('<int:pk>/update/', BaoCaoUpdate.as_view(), name="baocao_update"),
	path('<int:pk>/delete/', BaoCaoDelete.as_view(), name="baocao_delete"),

	path('baocao/<int:pk>/add_note/', AddNote.as_view(), name="add_note"),
]
