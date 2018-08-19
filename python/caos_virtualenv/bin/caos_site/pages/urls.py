from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^page0/', views.page0, name='page0'),
    url(r'^news/eHacks_OCI/', views.news_oci, name='eHacks_OCI'),
    ]