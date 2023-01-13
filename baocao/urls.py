from django.urls import path
from baocao.views import BaoCaoCreate

urlpatterns = [

	path('create/', BaoCaoCreate.as_view(), name="baocao_create"),


]
