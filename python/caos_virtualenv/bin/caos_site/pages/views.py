from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template

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
    return render(request, "postContent/eHacks_oci.html")

def events(request):
    return render(request, "miscPagesContent/events.html")

def register(request):
    return render(request, "miscPagesContent/register.html")

def officers(request):
    return render(request, "officers/officerContent.html")

def about(request):
    return render(request, "miscPagesContent/about.html")

def contact(request):
    return render(request, "miscPagesContent/contact.html")
