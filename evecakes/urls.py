from django.contrib import admin
from core import urls
from user import urls
from django.urls import path, include
from django.conf.urls.static import static
from .settings import MEDIA_URL,MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path("user/", include('user.urls', namespace='user')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
