from django.contrib import admin


from .models import EnergyUsage, Event, Laptop

admin.site.register(EnergyUsage)
admin.site.register(Event)
admin.site.register(Laptop)