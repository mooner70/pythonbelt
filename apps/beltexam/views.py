# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from .models import UserRegistration
from models import *
import bcrypt
def user_registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        b = User.objects.create(name=request.POST["name"], username=request.POST["username"], hiredate=request.POST["hiredate"], password=hash1)
        request.session['name'] = request.POST["name"]
        request.session["user_id"] = b.id
        return redirect("/dashboard")
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        user = User.objects.get(username = request.POST["username"])
        request.session['name'] = user.name
        request.session["user_id"] = user.id
        return redirect("/dashboard")
def index(request):
    return render(request, 'index.html')
def add(request):
    errors = Item.objects.add_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/wish_items/create")
    else:
        addedby = User.objects.get(name=request.session['name'])
        Item.objects.create(items=request.POST["items"], date_added = datetime.now(), users=addedby)
        return redirect("/dashboard")


def additem(request):
    return render(request, 'additem.html')
def logout(request):
    request.session.flush()
    return redirect('/')


def wishitems(request):
    return render(request, 'wish_items.html')



def dashboard(request):
    useritem = User.objects.get(id=request.session["user_id"])
    # d = User.objects.exclude(id=request.session["user_id"])
    context = {
        "items" : Item.objects.filter(users = useritem)
    }
        # "others_plans" : TravelPlans.objects.filter(user = d),
        # "joined_plans" : TravelPlans.objects.filter(travelers=request.session["user_id"])}
    return render(request, 'dashboard.html', context)


    
# def destination(request, id):
#     context = {
#         "travel_plans" : TravelPlans.objects.get(id=id)
#         }
#     return render(request, 'destination.html', context)
# def join(request, id):
#     userjoin = User.objects.get(id=request.session["user_id"])
#     e = TravelPlans.objects.get(id=id)
#     userjoin.trips.add(e)  
#     return redirect('/travels')
#     # e.travelers=request.session["user_id"]
