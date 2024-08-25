from django.urls import re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads.core import views


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^uploads$', views.upload, name='upload'),
    re_path(r'^download-translated-csv$', views.download_translated_csv, name='download_translated_csv'),
    re_path(r'^download-previously-translated-csv$', views.download_previously_translated_csv, name='download_previously_translated_csv'),
    re_path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
