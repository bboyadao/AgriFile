from django.urls import path
from user.views import ListUser, create_user

urlpatterns = [
    path('', ListUser.as_view(), name="user_list"),
    path('create/', create_user, name="user_create"),

]
