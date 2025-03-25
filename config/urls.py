from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('texnomart.urls'), name='texnomart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.urls import include, path

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns