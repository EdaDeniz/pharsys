from django.urls import path, re_path
from django.conf.urls import url
from patients.views import patient_create, patient_detail, patient_update, patient_delete, patient_search
from blog.views import post_list
from . import views

app_name = "patients"

urlpatterns = [

    path('patients/', views.patient_list, name='index'),


    re_path(r'^patients/create/', patient_create, name='create'),

    url(r'^patients/(?P<id>\d+)/$', patient_detail, name="detail"),

    url(r'^patients/(?P<id>\d+)/update/$', patient_update, name="update"),

    url(r'^patients/(?P<id>\d+)/delete/$', patient_delete, name="delete"),

    url(r'^patients/search/$', patient_search, name="search"),


]


