from lottery.views import lottery, lottery_single, save_lotto
from django.urls import path


app_name = 'lottery'


urlpatterns = [
    path('',lottery,name='lotto'),
    path('<int:pk>',lottery_single,name='lotto_single'),
    path('<int:pk>/<int:lotto>/<val>',save_lotto,name='lotto')
]
