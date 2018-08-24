from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegistrationForm

# Create your views here.

def index(request):
    template = loader.get_template('home.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def page0(request):
    return render(request, "post/page0.html")

def news_oci(request):
    return render(request, "postContent/eHacks_oci.html")

def weCode_2018(request):
    return render(request, "postContent/weCode_2018.html")

def mlh_localhost_drb(request):
    return render(request, "postContent/mlh_localhost_drb.html")

def events(request):
    return render(request, "miscPagesContent/events.html")

def register(request):
    return render(request, "miscPagesContent/registration.html")

def officers(request):
    return render(request, "officers/officerContent.html")

def about(request):
    return render(request, "miscPagesContent/about.html")

def contact(request):
    return render(request, "miscPagesContent/contact.html")

def success(request):
    return render(request, "miscPagesContent/success.html")

def register(request):
    args = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pages:success'))
    else:
        form = RegistrationForm()
        args['form'] = form

    return render(request,'miscPagesContent/registration.html', args)

def csSocial2018(request):
    return render(request, "postContent/2018_backToSchool_Social")
