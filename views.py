#from urllib import request
from django.shortcuts import render 
import requests 
import sys
from subprocess import run, PIPE

def button(request):
    return render(request,'home.html',None)

def output(request):
    data= requests.get("https://www.google.com/")
    print(data.text)
    data= data.text
    return render(request,'home.html', {'data':data})
    
def external(request):
    inp= request.POST.get('param')

    out= run ([sys.executable, 'C:\\Users\\HP\\Desktop\\django\\buttonpython\\test.py',inp] ,shell=False,stdout=PIPE )
    print(out)
    return render(request,'home.html',{'data1':out.stdout})

