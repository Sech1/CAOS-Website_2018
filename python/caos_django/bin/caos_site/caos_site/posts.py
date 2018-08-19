from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def news_oci(request):
    template = loader.get_template('/post/03-05-2018_eHacks_OCI.html')
    context = {
    }
    return HttpResponse(template.render(context, request))