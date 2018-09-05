from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import admin
from django import forms

from .forms import RegistrationForm
from .forms import SendEmailForm


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
        first = request.POST['first']
        last = request.POST['last']
        fullName = first + ' ' + last
        emailAdr = request.POST['email']
        subject, from_email, to = 'Thanks for registering for CAOS', 'no-reply@caos.cs.siue.edu', emailAdr
        html_content = render_to_string('email.html', {'name': fullName})  # render with dynamic value
        text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.

        if form.is_valid():
            form.save()
            # create the email, and attach the HTML version as well.
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect(reverse('pages:success'))
    else:
        form = RegistrationForm()
        args['form'] = form

    return render(request, 'miscPagesContent/registration.html', args)


def cssocial2018(request):
    return render(request, "postContent/2018_backToSchool_Social.html")


def clothingbuy2018(request):
    return render(request, "postContent/caos_clothing_groupbuy1.html")
