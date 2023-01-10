from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from AgriFile.views import index, Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('login/', Login.as_view()),
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('file/', include("file.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()