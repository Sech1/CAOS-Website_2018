from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('/caos/html/CAOS-Website_2018/python/caos_django/bin/caos_site/pages/templates/home.html')
    context = {
        'test' : 'This is also a test string',
        'test2' : ['1','2','3','4','5'],
        }
    return HttpResponse(template.render(context, request))
