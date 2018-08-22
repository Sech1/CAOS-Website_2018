# forms.py

from models import Registration
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__' # Django adds all fields you've described in Student
        # Then you could rename you fields labels, otherwise django will use names of model fields
        labels = {
            'first': 'First Name',
            'last': 'Last Name',
            'email': 'Email',
        }

    # Now you could describe all validation methods
    def clean_first(self):
        first = self.cleaned_data['first']
        if not first.isalpha():
            return ValidationError('First name must contain only letters')
        return first

    def clean_last(self):
        last= self.cleaned_data['last']
        if not last.isalpha():
            return ValidationError('First name must contain only letters')
        return last