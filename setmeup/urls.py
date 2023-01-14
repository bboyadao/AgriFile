from django.urls import path
from setmeup.views import ListUser, CreateUser, DetailUser, UpdateUser, ChangePassUser, DeleteUser, NoiNhanList, \
	NoiNhanDelete, NoiNhanUpdate, NoiNhanCreate, NoiNhanDetail, PhongBanList, PhongBanCreate, PhongBanDetail, \
	PhongBanUpdate, PhongBanDelete, LichBaoCaoList, LichBaoCaoCreate, LichBaoCaoDetail, LichBaoCaoUpdate, \
	LichBaoCaoDelete, AdminBaoCao
from baocao.views import BaoCaoCreate

urlpatterns = [
	path('user/', ListUser.as_view(), name="user_list"),
	path('user/create/', CreateUser.as_view(), name="user_create"),
	path('user/<str:slug>/', DetailUser.as_view(), name="user_detail"),
	path('user/<slug:slug>/update/', UpdateUser.as_view(), name="user_update"),
	path('user/<slug:slug>/set_pass/', ChangePassUser.as_view(), name="admin_set_user_pass"),
	path('user/<slug:slug>/change_pass/', ChangePassUser.as_view(), name="user_change_pass"),
	path('user/<slug:slug>/delete/', DeleteUser.as_view(), name="user_delete"),

	# noi nhan
	path('noinhan/', NoiNhanList.as_view(), name="noinhan_list"),
	path('noinhan/create/', NoiNhanCreate.as_view(), name="noinhan_create"),
	path('noinhan/<int:pk>/', NoiNhanDetail.as_view(), name="noinhan_detail"),
	path('noinhan/<int:pk>/update/', NoiNhanUpdate.as_view(), name="noinhan_update"),
	path('noinhan/<int:pk>/delete/', NoiNhanDelete.as_view(), name="noinhan_delete"),

	# Phong ban
	path('phongban/', PhongBanList.as_view(), name="phongban_list"),
	path('phongban/create/', PhongBanCreate.as_view(), name="phongban_create"),
	path('phongban/<int:pk>/', PhongBanDetail.as_view(), name="phongban_detail"),
	path('phongban/<int:pk>/update/', PhongBanUpdate.as_view(), name="phongban_update"),
	path('phongban/<int:pk>/delete/', PhongBanDelete.as_view(), name="phongban_delete"),

	# Lich Bao Cao
	path('lichbaocao/', LichBaoCaoList.as_view(), name="lichbaocao_list"),
	path('lichbaocao/create/', LichBaoCaoCreate.as_view(), name="lichbaocao_create"),
	path('lichbaocao/<int:pk>/', LichBaoCaoDetail.as_view(), name="lichbaocao_detail"),
	path('lichbaocao/<int:pk>/update/', LichBaoCaoUpdate.as_view(), name="lichbaocao_update"),
	path('lichbaocao/<int:pk>/delete/', LichBaoCaoDelete.as_view(), name="lichbaocao_delete"),



]
