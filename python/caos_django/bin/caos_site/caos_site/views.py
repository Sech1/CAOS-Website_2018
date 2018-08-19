from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('templates/home.html')
    context = {
        'test' : 'This is also a test string',
        'test2' : ['1','2','3','4','5'],
        }
    return HttpResponse(template.render(context, request))

def page0(request):
    template = loader.get_template('templates/post/page0.html')
    context = {
    }
    return HttpResponse(template.render(context, request))