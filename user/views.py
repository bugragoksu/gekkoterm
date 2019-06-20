from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .forms import WordForm,LoginForm,RegisterForm
from sozlukContent.models import SozlukContent
from django.contrib.auth import authenticate,login
# Create your views here.


def getWordsView(request):
    return render(request, 'user/getWords.html', {})


def wordCreate(request):

    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = WordForm()

    context = {
        'form': form,
    }
    return render(request, 'user/form.html', context)


def wordUpdate(request,id):
    post=get_object_or_404(SozlukContent,id=id)
    form=WordForm(request.POST or None,instance=post)
    
    if form.is_valid():
            form.save()
   
    context = {
        'form': form,
    }
    return render(request, 'user/form.html', context)

def wordDelete(request,id):
    post=get_object_or_404(SozlukContent,id=id)
    post.delete()
    return HttpResponseRedirect('/user/getWords')

def loginView(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('/')
    return render(request,'user/loginForm.html',{'form':form,'title':'Giriş Yap'})


def registerView(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
    
    return render(request,'user/loginForm.html',{'form':form,'title':'Giriş Yap'})