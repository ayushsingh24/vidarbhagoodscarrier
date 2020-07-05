from django.shortcuts import render,redirect
from .models import Booking
from django.contrib import messages
from django.contrib.auth.models import auth
from .forms import CustomerForm

def home(request):
    import json
    import requests

    if request.method == 'POST':
        search = request.POST['Booking']
        data = Booking.objects.filter(name=search)
    
    else:
        data = ""
    
    return render(request,'home.html',{'data' : data})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('owner')
        
        else:
            messages.info(request,'invalid credintials')
            return redirect('login')

    else:
        return render(request,'login.html',{})

def logout(request):
    auth.logout(request)
    return render(request,'logout.html',{})

def book(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request,'We got your booking.')
            return redirect('booking')
        else:
            messages.info(request,'Invalid information')
            return redirect('booking')
            
    else:
        return render(request,'booking.html',{})

def owner(request):
    if request.method == 'POST':
        freight = request.POST['freight']
        acceptance = request.POST['acceptance']
        id = request.POST['id']

        here = Booking.objects.get(pk=id)
        here.freight = freight
        here.acceptance = acceptance
        here.save()
        return redirect('owner')

    all_bookings = Booking.objects.all()
    return render(request,'owner.html',{'all_bookings' : all_bookings})