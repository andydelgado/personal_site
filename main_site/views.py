from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'main_site/index.html')

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(email=request.POST.get('email'), subject=request.POST.get('subject'), message=request.POST.get('message'))
        messages.success(request, 'Thanks for your message! I will get back to you soon!')
        return redirect('/')
    else:
        return render(request, 'main_site/contact.html')

def projects(request):
    return render(request, 'main_site/projects.html')