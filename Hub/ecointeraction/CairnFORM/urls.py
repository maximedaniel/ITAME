"""ecointeraction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'Monitor/(?P<hour1>[0-9]+)/(?P<hour2>[0-9]+)/', views.monitor1, name='Monitor'),
    url(r'Monitor/(?P<timestamp1>\d{4}-\d{2}-\d{2})/(?P<hour1>[0-9]+)/(?P<hour2>[0-9]+)/', views.monitor2, name='Monitor'),
    url(r'Sedyl/', views.sedyl, name='sedyl'),
    url(r'Script/', views.script, name='script'),
    url(r'Study/(?P<timestamp1>\d{4}-\d{2}-\d{2})/(?P<timestamp2>\d{4}-\d{2}-\d{2})/', views.studyFromTo, name='studyFromTo'),
    url(r'Json/(?P<timestamp1>\d{4}-\d{2}-\d{2})/(?P<timestamp2>\d{4}-\d{2}-\d{2})/', views.jsonFromTo, name='jsonFromTo'),
    url(r'Study/(?P<timestamp>\d{4}-\d{2}-\d{2})/', views.studyAt, name='studyAt'),
    url(r'Study/', views.study, name='study'),
    #url(r'users/', views.users, name='users'),
    #url(r'list/', views.list, name='list'),
    url(r'getEnergyUsageFromTo/(?P<year1>[0-9]+)/(?P<month1>[0-9]+)/(?P<day1>[0-9]+)/(?P<hour1>[0-9]+)/(?P<minute1>[0-9]+)/(?P<second1>[0-9]+)/(?P<year2>[0-9]+)/(?P<month2>[0-9]+)/(?P<day2>[0-9]+)/(?P<hour2>[0-9]+)/(?P<minute2>[0-9]+)/(?P<second2>[0-9]+)/', views.getEnergyUsageFromTo, name='energyUsageFromTo'),
   #url(r'getEnergyUsage/', views.getEnergyUsage, name='energyUsage'),
    url(r'getEventFromTo/(?P<year1>[0-9]+)/(?P<month1>[0-9]+)/(?P<day1>[0-9]+)/(?P<hour1>[0-9]+)/(?P<minute1>[0-9]+)/(?P<second1>[0-9]+)/(?P<year2>[0-9]+)/(?P<month2>[0-9]+)/(?P<day2>[0-9]+)/(?P<hour2>[0-9]+)/(?P<minute2>[0-9]+)/(?P<second2>[0-9]+)/', views.getEventFromTo, name='eventFromTo'),
    url(r'getLaptopFromTo/(?P<year1>[0-9]+)/(?P<month1>[0-9]+)/(?P<day1>[0-9]+)/(?P<hour1>[0-9]+)/(?P<minute1>[0-9]+)/(?P<second1>[0-9]+)/(?P<year2>[0-9]+)/(?P<month2>[0-9]+)/(?P<day2>[0-9]+)/(?P<hour2>[0-9]+)/(?P<minute2>[0-9]+)/(?P<second2>[0-9]+)/', views.getLaptopFromTo, name='laptopFromTo'),

    #url(r'getEvent/', views.getEvent, name='event'),
    #url(r'getByUsername/event/(?P<username>.*)/', views.getEventByUsername, name='eventByUsername'),
    #url(r'generate/', views.generate, name='generate'),
    #url(r'getForecast/(?P<hour_min>[0-9]+)/(?P<hour_max>[0-9]+)/', views.getForecast, name='getForecast'),
    #url(r'post/(?P<username>.*)/(?P<near>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<hour>[0-9]+)/(?P<minute>[0-9]+)/(?P<second>[0-9]+)/(?P<battery_level>[0-9]+)/(?P<charge_level>[0-9]+)/(?P<discharge_level>[0-9]+)/(?P<plugged>[0-9]+)/', views.post, name='post'),
    url(r'post/', views.post, name='post'),
]