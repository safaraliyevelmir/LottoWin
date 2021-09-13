import random

def captcha():
    
    cap_list = []
    n=0
    while(n<6):
        elem = {}
        num = random.randint(1,9)
        deg = random.randint(-20,100)

        for i in ['num','deg']:
            elem[i] = eval(i)
        cap_list.append(elem)
        n=n+1
        len = cap_list.__len__()
        if len >  6:
            cap_list.pop()
    return cap_list




