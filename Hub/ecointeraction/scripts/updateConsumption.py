from CairnFORM.models import EnergyUsage
from CairnFORM.models import Event
from django.utils import timezone

def run():
    usages = EnergyUsage.objects.all().order_by('timestamp')
    for usage in usages:
        timestamp = usage.timestamp
        min_frame = timestamp.replace(minute=0, second=0, microsecond=0)
        max_frame = timestamp.replace(minute=59, second=59, microsecond=0)
        events = Event.objects.exclude(timestamp__lt=min_frame)
        events = events.exclude(timestamp__gt=max_frame)

        min_frame = timestamp.replace(hour=min_frame.hour-1)
        max_frame = timestamp.replace(minute=59, second=59, microsecond=0)
        events = Event.objects.exclude(timestamp__lt=min_frame)
        events = events.exclude(timestamp__gt=max_frame)