from django.conf.urls import url
from django.urls import path, re_path
from medicines.views import *
from pharsys import settings
from . import views
from django.contrib.staticfiles.urls import static

app_name = "medicines"

urlpatterns = [

    re_path(r'^medicines/create/', medicine_create, name='createmed'),
    re_path(r'^medicines/list/', list_item, name='listmed'),
    url(r'^medicines/(?P<id>\d+)/$', medicine_detail, name="detail"),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
