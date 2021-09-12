from term_and_condination.models import TermAndCondition
from django.urls import path
from django.urls.conf import include

from .views import AboutPageView, IndexPageView, subscribe

from term_and_condination.views import PrivacyPolicyView, TermAndConditionView

app_name = 'core'


urlpatterns = [
    path('',IndexPageView.as_view(),name='index'),
    path('subscribe',subscribe,name='subscribe'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('privacy_policy/',PrivacyPolicyView.as_view(),name='privacy'),
    path('term_and_condination',TermAndConditionView.as_view(),name='term_and_cond')
]
