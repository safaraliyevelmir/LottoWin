from django.core.mail import send_mail
from announcment.forms import SubscribeForms
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.views.generic import TemplateView
from announcment.models import Subscriber
from .models import *
from django.contrib.auth import get_user_model
from lottery.models import Lottery
User = get_user_model()


class IndexPageView(TemplateView):
    template_name = 'index.html' 

    def get(self, request):
        visitor = get_object_or_404(Visitors.objects.filter(id=1))
        visitor.views += 1
        visitor.save()
        index = Index.objects.first()
        join =Join.objects.all()
        join_title =  JoinTitle.objects.first()
        faqs  = Faq.objects.all()
        sub_form = SubscribeForms()
        services = Service.objects.all()
        faq_img  = FaqImage.objects.first()
        user_count = User.objects.all().count()
        visitor = Visitors.objects.first()
        lotteries = Lottery.objects.all()[:5]
        winner_count = RecentWinner.objects.count()
        recent_winner = RecentWinner.objects.all()[:8]
        context = {
            'index':index,
            'join':join,
            'join_title':join_title,
            'faqs':faqs,
            'sub_form':sub_form,
            'services':services,
            'faq_img':faq_img,
            'user_count':user_count,   
            'visitor':visitor,
            'lotteries':lotteries,
            'winner_count':winner_count,
            'recent_winner':recent_winner,
        }
        return render(request,'index.html',context)
        

    

class AboutPageView(TemplateView):

    template_name = 'about.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] =  AboutUs.objects.first()
        context["services"] =  Service.objects.all()
        return context


def subscribe(request):
    if request.method == 'POST':
        form =  SubscribeForms(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            email = obj.email
            from_email = settings.EMAIL_HOST_USER
            to = [email]
            send_mail("Subscribe succesfully","You subscribe succesfully. We send announcment. Thanks!",from_email,to)
            return redirect('/')
    return redirect('/')



