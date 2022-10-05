from django.http import HttpResponse
from django.shortcuts import render

import random

# Create your views here.

def password(request):

    #a~z
    chars=[ chr(c) for c in range(97,123)]
    print(chars)
# 取得輸入的長度
length= eval(request.GET.get('length')) if request.GET.get('input-length')=='' \
    else eval(request.GET.get('input-length'))

# print(random.sample(chars,length))

password=[random.choice(chars) for i in range(length)]

print(password)
print(length)

    return render(request,'./password.html',{'password':123456})

def index(request):
    print('Hello Django')
   
    return render(request,'./index.html')
