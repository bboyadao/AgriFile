from django.urls import path
from user.views import ListUser

urlpatterns = [
    path('', ListUser.as_view()),
]
