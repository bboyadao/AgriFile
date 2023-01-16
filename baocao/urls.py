from django.urls import path
from baocao.views import BaoCaoCreateByNof, BaoCaoDetail, BaoCaoList, BaoCaoUpdate, BaoCaoDelete, AddNote, \
	BaoCaoQuickCreate

urlpatterns = [
	path('', BaoCaoList.as_view(), name="baocao_list"),
	path('create_by_nof/', BaoCaoCreateByNof.as_view(), name="baocao_create_by_nof"),
	path('quick_create/', BaoCaoQuickCreate.as_view(), name="baocao_quick_create"),

	path('<pk>/', BaoCaoDetail.as_view(), name="baocao_detail"),
	path('<int:pk>/update/', BaoCaoUpdate.as_view(), name="baocao_update"),
	path('<int:pk>/delete/', BaoCaoDelete.as_view(), name="baocao_delete"),

	path('baocao/<int:pk>/add_note/', AddNote.as_view(), name="add_note"),
]
