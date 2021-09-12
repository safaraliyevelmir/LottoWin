from django.urls import path
from django.urls.base import reverse_lazy

from .views import loginUser, logoutUser, register, success
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, MySetPasswordForm





urlpatterns = [
    path('register/',register,name='register'),
    path('success/<str:token>',success,name='success'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),


    path('reset_password/',
                            auth_views.PasswordResetView.as_view(
                                template_name = 'forgot-password.html',
                                form_class = UserPasswordResetForm
                            ),
                            name='reset_password'),

    path('reset_password_sent/',
                                auth_views.PasswordResetDoneView.as_view(
                                    template_name = 'password_reset_done.html'
                                ),
                                name='password_reset_done'),
    
    path('reset/<uidb64>/<token>',
                                auth_views.PasswordResetConfirmView.as_view(
                                    template_name = 'password_reset_confirm.html',
                                    form_class = MySetPasswordForm
                                ),
                                name='password_reset_confirm'),
    
    path('reset_password_complete/',
                                    auth_views.PasswordResetCompleteView.as_view(
                                        template_name = 'password_reset_complete.html'
                                    ),
                                    name='password_reset_complete'),

]   
