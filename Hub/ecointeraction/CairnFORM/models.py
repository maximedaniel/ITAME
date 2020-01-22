from __future__ import unicode_literals

from django.db import models


class EnergyUsage(models.Model):

    timestamp = models.DateTimeField(primary_key=True)
    production = models.FloatField(default=-1)
    consumption = models.FloatField(default=-1)
    raw_production = models.FloatField(default=-1)

    def __str__(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M') + ", raw_production (% capacity) : "+str(self.raw_production) + ", production (% capacity) : "+str(self.production)+", consumption (% of 50% depth charge) : "+str(self.consumption)


class Laptop(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    username = models.CharField(max_length=60, null=True)
    plugged =  models.IntegerField(null=True)
    near =  models.IntegerField(null=True)
    batteryLevel =  models.IntegerField(null=True)
    chargeLevel =  models.IntegerField(null=True)
    dischargeLevel =  models.IntegerField(null=True)
    availability = models.IntegerField(null=True)
    batteryRechargeTime = models.IntegerField(null=True)
    batteryStatus = models.IntegerField(null=True)
    caption = models.CharField(max_length=60, null=True)
    chemistry = models.IntegerField(null=True)
    configManagerErrorCode = models.IntegerField(null=True)
    configManagerUserConfig = models.IntegerField(null=True)
    creationClassName = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=60, null=True)
    designCapacity = models.IntegerField(null=True)
    designVoltage = models.IntegerField(null=True)
    deviceID = models.CharField(max_length=60, null=True)
    errorCleared = models.IntegerField(null=True)
    errorDescription = models.CharField(max_length=60, null=True)
    estimatedChargeRemaining = models.IntegerField(null=True)
    estimatedRunTime = models.IntegerField(null=True)
    expectedBatteryLife = models.IntegerField(null=True)
    expectedLife = models.IntegerField(null=True)
    fullChargeCapacity = models.IntegerField(null=True)
    lastErrorCode = models.IntegerField(null=True)
    maxRechargeTime = models.IntegerField(null=True)
    name = models.CharField(max_length=60, null=True)
    PNPDeviceID = models.CharField(max_length=60, null=True)
    powerManagementSupported = models.IntegerField(null=True)
    smartBatteryVersion = models.CharField(max_length=60, null=True)
    status = models.CharField(max_length=60, null=True)
    statusInfo = models.IntegerField(null=True)
    systemCreationClassName = models.CharField(max_length=60, null=True)
    systemName = models.CharField(max_length=60, null=True)
    timeOnBattery = models.IntegerField(null=True)
    timeToFullCharge = models.IntegerField(null=True)

    def __str__(self):
        return 'date('+self.timestamp.strftime('%Y-%m-%d %H:%M:%S') + "):user("+str(self.username)+ "):proximity("+str(self.near) + "):level("+ str(self.estimatedChargeRemaining) + "%):isPlugged(" + str(self.plugged) + ")"

class Event(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    username = models.CharField(max_length=60)
    near =  models.IntegerField()
    battery_level =  models.IntegerField()
    charge_level =  models.IntegerField()
    discharge_level =  models.IntegerField()
    plugged =  models.IntegerField()

    def __str__(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M:%S') + ":"+str(self.username)+ ":"+str(self.near) + ":"+str(self.battery_level) + ":"+str(self.charge_level) + ":"+str(self.discharge_level) + ":"+str(self.plugged)

#class User(models.Model):

#    mac_address = models.CharField(max_length=60)
#    ip_address = models.CharField(max_length=60)
#    timestamp = models.DateTimeField()
#    battery_level = models.IntegerField(default=0)
#    battery_events = models.ManyToManyField(BatteryEvent)
#
#    def __str__(self):
#        return "MAC: "+self.mac_address + " IP: "+self.ip_address + " LAST UPDATE: "+self.timestamp.strftime('%Y-%m-%d %H:%M')+" BATTERY LEVEL: "+str(self.battery_level)
