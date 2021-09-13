from django import template
from django.contrib.admin.decorators import register

register = template.Library()



def commofunc(value):
    value = str(value)
    list = []
    commo_index = 3
    for i in reversed(value):
        list.append(i)
        
        if list.__len__() == commo_index:
            list.append(",")
            commo_index=commo_index+4


    if list[-1] == ',':
        list = list[:-1]    


    mainlist = []
    for i in reversed(list):
        
        mainlist.append(i)

    number = ''.join(mainlist)
    return number


register.filter('commofunc',commofunc)





    

    
    
