from django.urls import path
from user.views import ChangePassUser, UserDetail

urlpatterns = [
    path('<slug:slug>/set_pass/', ChangePassUser.as_view(), name="admin_set_user_pass"),
    path('me/', UserDetail.as_view(), name="me"),
]
