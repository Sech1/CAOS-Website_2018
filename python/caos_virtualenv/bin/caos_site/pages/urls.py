from django.urls import include, path
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^$', views.index , name='index'),
    path('postContent/0', views.news_oci, name='eHacks_OCI'),
    path('postContent/1', views.mlh_localhost_drb, name='mlh_localhost'),
    path('postContent/2', views.weCode_2018, name='weCode_2018'),
    path('postContent/3', views.cssocial2018, name='cssocial2018'),
    path('postContent/4', views.clothingbuy2018, name='clothingbuy2018'),
    path('postContent/5', views.csSocialPost, name='social2018post'),
    path('postContent/6', views.mlhlocalpost, name='mlhlocalpost'),
    path('registration/success', views.success, name='success'),
    path('page0/', views.page0, name ='page0'),
    path('events/', views.events, name='events'),
    path('register/', views.register, name='register'),
    path('officers/', views.officers, name='officers'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('registration/success', views.success, name='success'),
    #url(r'^post/page0/', views.page0, name='page0'),
    #url(r'^/post/postContent/eHacks_OCI/', views.news_oci, name='eHacks_OCI'),
    ]
