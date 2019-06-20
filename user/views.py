from django.shortcuts import render

# Create your views here.

def registerView(request):
    return render(request,'user/register.html',{})



def loginView(request):
    return render(request,'user/login.html',{})