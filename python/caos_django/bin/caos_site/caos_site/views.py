from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import posts

# Create your views here.

def index(request):
    template = loader.get_template('home.html')
    context = {
        }
    return HttpResponse(template.render(context, request))

def page0(request):
    template = loader.get_template('post/page0.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def news_oci(request):
    template = loader.get_template('/post/postContent/03-05-2018_eHacks_OCI.html')
    context = {
    }
    return HttpResponse(template.render(context, request))