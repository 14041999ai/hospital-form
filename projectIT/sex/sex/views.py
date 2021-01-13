from django.http import  HttpResponse
from django.shortcuts import  render

def index(request ):
    #params ={'name':'abhishek','site':'Xxxx.com'}
    return render(request,'index.html')
   # return HttpResponse(" sexy abhishek and handsome like rithik roshan")
def khalifa(request ):
    return HttpResponse(" mia khalifa wear glasses")
def leone(request ):
    return HttpResponse(" leone is porn star")
def jzeey(request ):
    return HttpResponse(" jzeey is sexy")
    text= request.GET.get('text','default')
    print(text)
