"""caos_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from . import views
from . import posts
from django.conf.urls import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page0/$', views.page0, name='page0'),
    url(r'^news/oci$', posts.news_oci, name='eHacks_OCI'),
    #url(r'^index/', include(("caos_site.views.index", 'index'), namespace='index')),
]
