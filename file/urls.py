from django.urls import path

from file.views import FileList

urlpatterns = [
    path('', FileList.as_view()),
]
