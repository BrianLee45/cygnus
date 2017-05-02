# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . models import Trip
from ..loginReg.models import User
from django.contrib import messages

# Create your views here.
def index(request):

    if 'id' not in request.session:
        return redirect('login:home')
    else:
        response, objTrips = Trip.objects.GetMyTrips(request.session['id'])
        response, objOthers = Trip.objects.GetOtherPeopleTrips(request.session['id'])
        context = {
            "trips": objTrips,
            "otherTrips": objOthers
        }
        return render(request, 'thor/index.html', context)

def showAdd(request):

    return render(request, 'thor/addtrip.html')

def addTrip(request):

    user_id = request.session['id']

    response, objReturn = Trip.objects.CreateTrip(request.POST, user_id)

    if response:
        return redirect('thor:home')
    else:
        for error in objReturn:
            messages.error(request, error)
        return redirect('thor:showAdd')

def joinTrip(request, trip_id):

    response, objReturn = Trip.objects.doJoinTrip(request.session['id'], trip_id)

    if not response:
        for error in objReturn:
            messages.error(request, error)

    return redirect('thor:home')

def showDestination(request, trip_id):

    response, objReturn = Trip.objects.GetOneTrip(trip_id)
    response, objTravelers = Trip.objects.GetOtherTravelers(trip_id)

    context = {
        "trip": objReturn,
        "travelers": objTravelers
    }

    print objTravelers
    return render(request, 'thor/destination.html', context)
