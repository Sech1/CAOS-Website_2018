from django.urls import path
from django.views.genertic import TemplateView
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^', views.index , name='index'),
    url(r'^page0/$', views.page0, name='page0'),
    url(r'^eHacks_OCI/$', views.news_oci, name='eHacks_OCI'),
    ]