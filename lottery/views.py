from datetime import datetime
from django.db.models.lookups import In
from lottery.models import Lottery, Ticket
from django.shortcuts import redirect, render
from lottery.utils import number
from django.core.mail import  send_mail
from django.conf import settings




def lottery(request):
    lotteries = Lottery.objects.all()


    context = {
        'lotteries':lotteries
    }

    return render(request,'lotteries.html',context)

def lottery_single(request,pk):
    lottery = Lottery.objects.filter(pk=pk).first() 
    lotteryc = Ticket.objects.filter(lottery=pk).count()
    one_hundread_func = one_hundread(pk)



    context = {
        'lottery':lottery,
        'lotteryc':lotteryc,
        'one_hundread':one_hundread_func,
    }

    return render(request,'lottery.html',context)

def save_lotto(request,pk,lotto,val):
    lottery = Lottery.objects.filter(pk=pk).first()
    user = request.user
    numbers = number(val)
    for i in numbers:
        i = int(i)
        Ticket.objects.create(user=user,lottery=lottery,number=i)
    
    num = ', '.join(numbers)
    
    send_ticket_mail(lotto,num,user.email)

    return redirect('/')

def send_ticket_mail(price,numbers,email):
    
    subject  = 'You buy ticket successfully'
    message = f'You pay {price} manat and you play for {numbers}'
    send_email = settings.EMAIL_HOST_USER
    rec_list = [email]
    send_mail(subject,message,send_email,rec_list)

def one_hundread(pk):
    tickets = []
    list = []
    ticket = Ticket.objects.filter(lottery=pk).all()
    for a in ticket:
        tickets.append(a.number)
    for i in range(1,101):
        object = {}
        if i in tickets:
            object = {
                'number':i,
                'disabled':'disabled'
            }
            list.append(object)
        else:
            object = {
                'number':i,
                'disabled':''
            }
            list.append(object)
    return list

