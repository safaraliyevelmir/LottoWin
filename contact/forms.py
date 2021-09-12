from .models import Contact
from django import forms
from django.utils.translation import gettext as _

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','subject','message']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form--control','placeholder':_('Your Name')}),
            'email':forms.EmailInput(attrs={'class':'form--control','placeholder':'Enter E-Mail Address'}),
            'subject':forms.TextInput(attrs={'class':'form--control','placeholder':'Write your subject'}),
            'message':forms.Textarea(attrs={'class':'form--control','placeholder':'Write your message'}),
        }