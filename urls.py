
from django.urls import re_path as url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button),
    url(r'^output', views.output, name="script"),
    url(r'^external', views.external),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
