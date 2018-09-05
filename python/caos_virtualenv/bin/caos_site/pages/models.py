from django.db import models
from datetime import datetime
from . import mass_email

# Create your models here.

class Registration(models.Model):
    first = models.CharField("First", max_length=50)
    last = models.CharField("Last", max_length=50)
    email = models.EmailField()

class MailText(models.Model):
    subject = models.CharField("Subject", max_length=1000)
    header = models.CharField("Header", max_length=1000)
    message = models.CharField("Message", max_length=25000)
    send_it = models.BooleanField(default=False) #check it if you want to send your email

    def save(self):

        template_path = 'admin/email_template.html'
        email_context = {
            'email_header' : self.header,
            'email_body' : self.message,
        }

        if self.send_it:
            #First you create your list of users
            user_list = []
            test_list = ['jaschoo@siue.edu', 'braburk@siue.edu']
            user_list = Registration.objects.values_list('email', flat=True)

            #Then you can send the message.
            mass_email.send_mass_html_mail(
                self.subject,
                template_path,
                email_context,
                test_list,
            )

    class Meta:
        verbose_name = "Emails to send"
        verbose_name_plural = "Emails to send"