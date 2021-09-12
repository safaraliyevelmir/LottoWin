from django.forms import widgets
from .models import Subscriber
from django import forms
from django.utils.translation import gettext_lazy as _

class SubscribeForms(forms.ModelForm):
    
    class Meta:
        model = Subscriber
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={"class":"form--control","placeholder":_('Email Address')})
        }