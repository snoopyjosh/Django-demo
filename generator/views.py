from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def password(request):

    #a~z
    chars=[ chr(c) for c in range(97,123)]
    print(chars)

    input_length=request.GET.get('input_length')
    print(input_length)

    return render(request,'./password.html',{'password':123456})

def index(request):
    print('Hello Django')
   
    return render(request,'./index.html')
