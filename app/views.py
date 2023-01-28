from django.shortcuts import render
from app.views import *
from django.http import HttpResponse
# Create your views here.
def html_form(request):
    if request.method=='POST':
        un=request.POST['usn']
        pw=request.POST['psw']
        print(un)
        print(pw)
        return HttpResponse('data is submitted')
    return render(request,'html_form.html')