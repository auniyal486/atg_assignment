from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from . import models
from django.contrib.auth.models import User

#login and sigin page view
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("atg_app:home"))
    if request.method=="POST":
        if len(request.POST)==3:
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('atg_app:home'))
                else:
                    messages.add_message(request,messages.ERROR,"account is not active")
                    return HttpResponseRedirect(reverse('atg_app:index'))
            else:
                messages.add_message(request,messages.ERROR,"invalid details")
                return HttpResponseRedirect(reverse('atg_app:index'))
        else:
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            if(len(User.objects.filter(username=username))!=0): 
                messages.add_message(request,messages.ERROR,"choose another username")
                return HttpResponseRedirect(reverse('atg_app:index'))
            elif(len(User.objects.filter(email=email))!=0):
                messages.add_message(request,messages.ERROR,"choose another email")
                return HttpResponseRedirect(reverse('atg_app:index'))
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                login(request,user)
                return HttpResponseRedirect(reverse('atg_app:home'))
    return render(request,"index.html",context={'signin_form':forms.SignupForm(),'login_form':forms.LoginForm()}) 

#state page view
@login_required
def home(request):
    states=models.States.objects.all()
    return render(request,'home.html',context={'states':states,'current_user':request.user.username})

#category page view
@login_required
def category_data(request,**kwargs):
    categories=models.JobType1.objects.all()
    return render(request,'categories.html',context={'categories':categories,'state':kwargs['state'],'current_user':request.user.username})

#subcategory page view
@login_required
def subcategory_data(request,**kwargs):
    subcategories=models.JobType2.objects.filter(Category=models.JobType1.objects.get(id=kwargs['cat']).Category)
    return render(request,'subcategories.html',context={'subcategories':subcategories,'state':kwargs['state'],'cat':kwargs['cat'],'current_user':request.user.username})

#jobs page view
@login_required
def jobs_data(request,**kwargs):
    companies=models.CompanyDetails.objects.all()
    jobs=models.Jobs.objects.filter(State=kwargs['state']).filter(Subcategory=models.JobType2.objects.get(id=kwargs['subcat']).Subcategory)
    return render(request,'jobs.html',context={'jobs':jobs,'current_user':request.user.username,'companies':companies,'state':kwargs['state'],'cat':kwargs['cat'],'subcat':kwargs['subcat']})

#a particular job page view
@login_required
def job_details(request,**kwargs):
    job=models.Jobs.objects.get(id=kwargs['job'])
    return render(request,'job_details.html',context={'job':job,'current_user':request.user.username})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('atg_app:index'))