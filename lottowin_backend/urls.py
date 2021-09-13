from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from contact.views import CreateContactView
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('i18n/',include('django.conf.urls.i18n')),

]


urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('',include('core.urls')),  
    path('accounts/',include('base_user.urls')),
    path('blog/',include('blog.urls')),
    path('lottery/',include('lottery.urls')),
    path('contact/',CreateContactView.as_view(),name='contact'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

