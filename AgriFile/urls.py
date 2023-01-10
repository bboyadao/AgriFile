from django.contrib import admin
from django.urls import path, include
from AgriFile.views import index, Login

urlpatterns = [
    path('', index),
    path('login/', Login.as_view()),
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('file/', include("file.urls")),
]
