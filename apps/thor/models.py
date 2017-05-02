# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..loginReg.models import User
from datetime import datetime, date
from django.db import models

# Create your models here.
class TripManager(models.Manager):
    def CreateTrip(self, request, user_id):
        print "func CreateTrip"

        errors = []

        if len(request['destination']) == 0:
            errors.append("Destination cannot be empty")

        if len(request['description']) == 0:
            errors.append("Description cannot be empty")

        datToday = date.today()
        print datToday

        if len(request['start_date']) == 0:
            errors.append("Start date cannot be empty")
        elif len(request['end_date']) == 0:
            errors.append("End date cannot be empty")
        else:
            datStart = datetime.strptime(request['start_date'], "%Y-%m-%d").date()
            datEnd = datetime.strptime(request['end_date'], "%Y-%m-%d").date()
            if datStart < datToday:
                errors.append("Start date cannot be earlier than today")

            if datEnd < datToday:
                errors.append("End date cannot be earlier than today")

            if datEnd < datStart:
                errors.append("The end date cannot be earlier than the start date")

        if len(errors) == 0:
            print "here"
            objUser = User.objects.GetUser(user_id)[0]
            print objUser
            try:
                objReturn = Trip.objects.create(
                    planner = objUser,
                    destination = request['destination'],
                    description = request['description'],
                    start_date = datetime.strptime(request['start_date'], "%Y-%m-%d").date(),
                    end_date = datetime.strptime(request['end_date'], "%Y-%m-%d").date()
                    # start_date = datetime.strptime(request['start_date'], "%m/%d/%Y").date(),
                    # end_date = datetime.strptime(request['end_date'], "%m/%d/%Y").date()
                    # birthday = datetime.strptime(request['birthday'], "%m/%d/%Y").date()  %m/%d/%Y
                )
                print "there"
                return (True, objReturn)
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                errors.append(e.message)
                return (False, errors)

        else:
            return (False, errors)

    def GetMyTrips(self, user_id):

        objReturn = Trip.objects.filter(planner__id=user_id)

        return(True, objReturn)


    def GetOneTrip(self, trip_id):

        try:
            objReturn = Trip.objects.get(id=trip_id)
            return (True, objReturn)
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            errors.append(e.message)
            return (False, errors)


    def GetOtherPeopleTrips(self, user_id):

        objReturn = Trip.objects.exclude(travelers__id=user_id)

        return(True, objReturn)

    def GetOtherTravelers(self, trip_id):

        objReturn = Trip.objects.get(id=trip_id).travelers.all()

        return (True, objReturn)


    def doJoinTrip(self, user_id, event_id):

        objUser = User.objects.GetUser(user_id)[0]

        try:
            objEvent = Trip.objects.get(id=event_id)
            objEvent = objEvent.travelers.add(objUser)
            return(True, objEvent)
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            errors.append(e.message)
            return (False, errors)


class Trip(models.Model):
    planner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    destination = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    travelers = models.ManyToManyField(User, related_name="all_travelers")
    objects = TripManager()

# class TripMembership(models.Model):
#     travelgroup = models.ForeignKey(Trip, on_delete=models.CASCADE)
#     person = models.ForeignKey(User, on_delete=models.CASCADE)
    # inviter = models.ForeignKey(
    #     Person,
    #     on_delete=models.CASCADE,
    #     related_name="membership_invites",
    # )
    # invite_reason = models.CharField(max_length=64)
