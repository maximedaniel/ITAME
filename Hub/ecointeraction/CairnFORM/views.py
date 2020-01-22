from django.shortcuts import render
import datetime
from .models import EnergyUsage, Event, Laptop
from django.db.models import Avg, Max, Min
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from .EpicesParser import EpicesParser
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt

import pandas as pd
import requests, zipfile, io
import json
import pytz
import numpy as np
from django.db.models import Count, Avg, Sum, Max


debug = True

old_usages = []

def getMaxChargeLevelAt(timestamp):
    min_frame = timestamp.replace(minute=0, second=0, microsecond=0)
    max_frame = timestamp.replace(minute=59, second=59, microsecond=0)
    events = Event.objects.exclude(timestamp__lt=min_frame)
    events = events.exclude(timestamp__gt=max_frame)
    if len(events):
        total_charge_by_user = list(events.values('username').annotate(Sum('charge_level')).aggregate(Max('charge_level__sum')).values())
        return total_charge_by_user[0]
    else:
        return 0


def index(request):
    return render(request, 'CairnFORM/index.html')
    #timestamp = timezone.now()
    #return getUsersNearFromTo(timestamp)

def sedyl(request):
    frame = timezone.now()
    min_frame = frame.replace(hour=0, minute=0, second=0)
    max_frame = frame.replace(hour=23, minute=59, second=59)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    #if len(usages) == 0 :
    #    generateEnergyUsage(request)
    #    return getEnergyUsageFromTo(request, year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2)

    return render(request, 'sedyl/index.html', locals())

@csrf_exempt
def script(request):
    if request.method == 'GET':
        return HttpResponse("ERROR")

    elif request.method == 'POST':
        return HttpResponse("OK")


def study(request):
    frame = timezone.now()
    min_frame = frame.replace(hour=0, minute=0, second=0)
    max_frame = frame.replace(hour=23, minute=59, second=59)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    events = Event.objects
    events = events.exclude(timestamp__lt=min_frame)
    events = events.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    events = events.order_by('timestamp')
    return render(request, 'CairnFORM/etude.html', locals())
    #timestamp = timezone.now()
    #return getUsersNearFromTo(timestamp)

def vis(request):
    frame = timezone.now()
    min_frame = frame.replace(hour=0, minute=0, second=0)
    max_frame = frame.replace(hour=23, minute=59, second=59)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    return render(request, 'CairnFORM/vis.html', locals())


def monitor1(request, hour1, hour2):
    global debug
    now_frame = timezone.now() + datetime.timedelta(hours=2)
    min_frame = now_frame.replace(hour=8, minute=0, second=0, microsecond = 0)
    max_frame = now_frame.replace(hour=17, minute=0, second=0, microsecond = 0)
    #print(min_frame," ",now_frame," ",max_frame)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    min_frame = now_frame.replace(hour=int(hour1), minute=0, second=0, microsecond = 0)
    max_frame = now_frame.replace(hour=int(hour2), minute=0, second=0, microsecond = 0)
    if debug : print("monitor1 : ", usages)
    #return HttpResponse(serializers.serialize("json", filter(usages)))

    return render(request, 'CairnFORM/monitor.html', locals())

def monitor2(request, timestamp1, hour1, hour2):
    now_frame = timezone.now() + datetime.timedelta(hours=2)
    min_frame = datetime.datetime.strptime(timestamp1, "%Y-%m-%d").replace(hour=int(hour1), minute=0, second=0)
    max_frame = datetime.datetime.strptime(timestamp1, "%Y-%m-%d").replace(hour=int(hour2), minute=0, second=0)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    return render(request, 'CairnFORM/monitor_past.html', locals())

def studyAt(request, timestamp):
    frame = datetime.datetime.strptime(timestamp, "%Y-%m-%d")
    min_frame = frame.replace(hour=0, minute=0, second=0)
    max_frame = frame.replace(hour=23, minute=59, second=59)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    events = Event.objects
    events = events.exclude(timestamp__lt=min_frame)
    events = events.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    events = events.order_by('timestamp')
    #if len(usages) == 0 :
    #    generateEnergyUsage(request)
    #    return getEnergyUsageFromTo(request, year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2)

    return render(request, 'CairnFORM/etude.html', locals())

def studyFromTo(request, timestamp1, timestamp2):
    min_frame = datetime.datetime.strptime(timestamp1, "%Y-%m-%d")
    max_frame = datetime.datetime.strptime(timestamp2, "%Y-%m-%d")
    max_frame = max_frame.replace(hour=23, minute=59, second=59)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    events = Event.objects
    events = events.exclude(timestamp__lt=min_frame)
    events = events.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    events = events.order_by('timestamp')
    #if len(usages) == 0 :
    #    generateEnergyUsage(request)
    #    return getEnergyUsageFromTo(request, year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2)

    return render(request, 'CairnFORM/etude.html', locals())

def jsonFromTo(request, timestamp1, timestamp2):
    min_frame = datetime.datetime.strptime(timestamp1, "%Y-%m-%d")
    max_frame = datetime.datetime.strptime(timestamp2, "%Y-%m-%d")
    max_frame = max_frame.replace(hour=23, minute=59, second=59)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    events = Event.objects
    events = events.exclude(timestamp__lt=min_frame)
    events = events.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    events = events.order_by('timestamp')
    #if len(usages) == 0 :
    #    generateEnergyUsage(request)
    #    return getEnergyUsageFromTo(request, year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2)

    return HttpResponse(serializers.serialize("json", events))

def users(request):
    events = Event.objects.all()
    return render(request, 'CairnFORM/users.html', locals())

def generateEnergyUsage(request):
    epicesParser = EpicesParser('6bm-cRpuq5X3HwdphKU5x8lInv4')
    epicesParser.update()
    times = epicesParser.times
    productions = epicesParser.forecasts
    for timestamp, production in zip(times, productions):
        try :
            usage = EnergyUsage.objects.get(timestamp=timestamp)
            usage.raw_production = production
            usage.save()
        except :
            usage = EnergyUsage(timestamp=timestamp, raw_production = production, production=0, consumption=0)
            usage.save()

    return HttpResponse("Done.")


def getEnergyUsageFromTo(request, year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2):
    global debug
    now_frame = timezone.now() + datetime.timedelta(hours=2)
    now_frame = now_frame.replace(year=int(year1), month=int(month1), day=int(day1))
    min_frame = now_frame.replace(year=int(year1), month=int(month1), day=int(day1), hour=8, minute=0, second=0, microsecond=0)
    max_frame = now_frame.replace(year=int(year2), month=int(month2), day=int(day2), hour=17, minute=0, second=0, microsecond=0)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    if debug : print("getEnergyUsageFromTo : ", usages)
    return HttpResponse(serializers.serialize("json", usages))

def getEventFromTo(request, year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2):
    min_frame = timezone.now()
    max_frame = timezone.now()
    min_frame = min_frame.replace(year=int(year1), month=int(month1), day=int(day1), hour=int(hour1), minute=int(minute1), second=int(second1), microsecond=0)
    max_frame = max_frame.replace(year=int(year2), month=int(month2), day=int(day2), hour=int(hour2), minute=int(minute2), second=int(second2), microsecond=0)
    events = Event.objects
    events = events.exclude(timestamp__lt=min_frame)
    events = events.exclude(timestamp__gt=max_frame)
    events = events.order_by('timestamp')
    if len(events) > 0 :
        return HttpResponse(serializers.serialize("json", events))
    else :
        return HttpResponse("Empty.")

def getEventByUsername(request, username):
    events = Event.objects.filter(username=username)
    events = events.order_by('timestamp')
    if len(events) > 0 :
        return HttpResponse(serializers.serialize("json", events))
    else :
        return HttpResponse("Empty")

def operate(start_timestamp):
    start_timestamp = start_timestamp.replace(minute=0, second=0, microsecond=0)
    now_timestamp = timezone.now()
    while start_timestamp < now_timestamp:
        consumption = min(1., getMaxChargeLevelAt(start_timestamp)/50)
        try :
            usage = EnergyUsage.objects.get(timestamp=start_timestamp)
            usage.consumption=consumption
            usage.save()
        except :
            usage = EnergyUsage(timestamp=start_timestamp, raw_production=0, production=0, consumption=consumption)
            usage.save()
        start_timestamp += datetime.timedelta(hours=1)

@csrf_exempt
def post(request):
    if(request.method == "POST"):
        try:
            jsonEvent = json.loads(request.body.decode('utf-8'))
            laptop = Laptop(
                timestamp = jsonEvent['Timestamp'],
                username = jsonEvent['Username'],
                plugged = jsonEvent['Plugged'],
                near = jsonEvent['Near'],
                batteryLevel = jsonEvent['BatteryLevel'],
                chargeLevel = jsonEvent['ChargeLevel'],
                dischargeLevel = jsonEvent['DischargeLevel'],
                availability = jsonEvent['Availability'],
                batteryRechargeTime = jsonEvent['BatteryRechargeTime'],
                batteryStatus = jsonEvent['BatteryStatus'],
                caption = jsonEvent['Caption'],
                chemistry = jsonEvent['Chemistry'],
                configManagerErrorCode = jsonEvent['ConfigManagerErrorCode'],
                configManagerUserConfig = jsonEvent['ConfigManagerUserConfig'],
                creationClassName = jsonEvent['CreationClassName'],
                description = jsonEvent['Description'],
                designCapacity = jsonEvent['DesignCapacity'],
                designVoltage = jsonEvent['DesignVoltage'],
                deviceID = jsonEvent['DeviceID'],
                errorCleared = jsonEvent['ErrorCleared'],
                errorDescription = jsonEvent['ErrorDescription'],
                estimatedChargeRemaining = jsonEvent['EstimatedChargeRemaining'],
                estimatedRunTime = jsonEvent['EstimatedRunTime'],
                expectedBatteryLife = jsonEvent['ExpectedBatteryLife'],
                expectedLife = jsonEvent['ExpectedLife'],
                fullChargeCapacity = jsonEvent['FullChargeCapacity'],
                lastErrorCode = jsonEvent['LastErrorCode'],
                maxRechargeTime = jsonEvent['MaxRechargeTime'],
                name = jsonEvent['Name'],
                PNPDeviceID = jsonEvent['PNPDeviceID'],
                powerManagementSupported = jsonEvent['PowerManagementSupported'],
                smartBatteryVersion = jsonEvent['SmartBatteryVersion'],
                status = jsonEvent['Status'],
                statusInfo = jsonEvent['StatusInfo'],
                systemCreationClassName = jsonEvent['SystemCreationClassName'],
                systemName = jsonEvent['SystemName'],
                timeOnBattery = jsonEvent['TimeOnBattery'],
                timeToFullCharge = jsonEvent['TimeToFullCharge']
                )
            laptop.save()
            return HttpResponse('OK')
        except Exception as e:
            print(e)
            return HttpResponse('NOT OK')
    return HttpResponse('NOT OK')

def getLaptopByUsername(request, username):
    laptops = Laptop.objects.filter(username=username)
    laptops = laptops.order_by('timestamp')
    if len(laptops) > 0 :
        return HttpResponse(serializers.serialize("json", laptops))
    else :
        return HttpResponse("Empty")

def getLaptopFromTo(request, year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2):
    min_frame = timezone.now()
    max_frame = timezone.now()
    min_frame = min_frame.replace(year=int(year1), month=int(month1), day=int(day1), hour=int(hour1), minute=int(minute1), second=int(second1), microsecond=0)
    max_frame = max_frame.replace(year=int(year2), month=int(month2), day=int(day2), hour=int(hour2), minute=int(minute2), second=int(second2), microsecond=0)
    laptops = Laptop.objects
    laptops = laptops.exclude(timestamp__lt=min_frame)
    laptops = laptops.exclude(timestamp__gt=max_frame)
    laptops = laptops.order_by('timestamp')

    if len(laptops) > 0 :
        return HttpResponse(serializers.serialize("json", laptops))
    else :
        return HttpResponse("Empty.")

#def post(request, username, near, year, month, day, hour, minute, second, battery_level, charge_level, discharge_level, plugged):
#    timestamp = timezone.now()
#    timestamp=timestamp.replace(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute), second=int(second))
#    event = Event(timestamp=timestamp, username=username, near=near, battery_level=battery_level, charge_level=charge_level, discharge_level=discharge_level, plugged=plugged)
#    event.save()
#    if int(near) == 1 and int(charge_level) > 0:
#        new_timestamp = timestamp.replace(minute=0, second=0, microsecond=0)
#        consumption = min(1., getMaxChargeLevelAt(new_timestamp)/50.)
#        try :
#            usage = EnergyUsage.objects.get(timestamp=new_timestamp)
#            usage.consumption=consumption
#            usage.save()
#        except :
# usage = EnergyUsage(timestamp=new_timestamp, raw_production = 0, production=0, consumption=consumption)
#           usage.save()
#    return HttpResponse('Ok')

