from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import ContactForm

# Create your views here.

def home(request):
    projects = Projects.objects.all()
    education = Eduction.objects.all()
    profile = image.objects.all()
    resume = Filefield.objects.all()
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Messages is Submitted Successfully")
            return redirect('/home/')
    else:
        form = ContactForm()
    return render(request,'index.html',{'education':education,'projects':projects,'form':form,'profile':profile ,'resume':resume})


def about(request):
    profile = image.objects.all()
    return render(request,'about.html',{'profile':profile})


def eduction(request):
    education = Eduction.objects.all()
    course = Course.objects.all()
    return render(request,'education.html',{'education':education,'course':course})
   

def project(request):
    projects = Projects.objects.all()
    return render(request,'Projects.html',{'projects':projects})



def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your form is Submitted Successfully")
            return redirect('/contact/')
    else:
        form = ContactForm()

    return render(request,'contact.html' , {'form':form})
    return render(request,'index.html')