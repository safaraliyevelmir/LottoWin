from .forms import ContactForm
from .models import Contact, ContactInformation, ContactTitle
from django.shortcuts import render

from django.views.generic import CreateView



class CreateContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = ContactInformation.objects.all()
        context['contact_title'] = ContactTitle.objects.first()
        return context
    