from django.urls import path
from user.views import ListUser, CreateUser, DetailUser, UpdateUser

urlpatterns = [
    path('', ListUser.as_view(), name="user_list"),
    path('create/', CreateUser.as_view(), name="user_create"),
    path('<str:slug>/', DetailUser.as_view(), name="user_detail"),
    path('<slug:slug>/update/', UpdateUser.as_view(), name="update_detail"),


]
