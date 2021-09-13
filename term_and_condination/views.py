from django.shortcuts import render
from django.views.generic.base import TemplateView


from .models import PrivacyPolicy, TermAndCondition

class PrivacyPolicyView(TemplateView):

    template_name = 'privacy-policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["privacypolicy"] = PrivacyPolicy.objects.first()
        return context


class TermAndConditionView(TemplateView):

    template_name = 'terms-and-condition.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["term"] = TermAndCondition.objects.first()
        return context
    
    
