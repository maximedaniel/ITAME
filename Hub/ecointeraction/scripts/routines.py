from CairnFORM.models import EnergyUsage
from CairnFORM.EpicesParser import EpicesParser
from django.utils import timezone
import datetime
import numpy as np
debug = True

def raw_variations(usages):
    variations = [0]
    for i in range(1, len(usages)-1):
        prev_production = usages[i-1].production
        curr_production = usages[i].production
        next_production = usages[i+1].production
        if prev_production > curr_production and next_production > curr_production:
            variations.append(i)
    variations.append(len(usages))
    return variations

def now(usages, now_hour):
    index_now = len(usages)-1
    for i in range(len(usages)-1):
        if usages[i].timestamp.hour == now_hour:
                index_now = i
    return index_now

def filtering(usages, now_hour, min_hour, max_hour):
    global debug
    if debug : print("FILTERING(USAGES, NOW_HOUR, MIN_HOUR, MAX_HOUR)")
    index_now = now(usages, now_hour)
    indexes_variations = raw_variations(usages)
    if debug : print("i_now : ", index_now)
    if debug : print(" i_variations : ", indexes_variations)

    # filtering variation
    decharge_duration = 3
    threshold = 0.12
    if debug : print("raw production : ", [usages[j].raw_production for j in range(len(usages))])
    if debug : print("filtered production : ", [usages[j].production for j in range(len(usages))])

    for i in range(len(indexes_variations)-1):
            variation = [usages[j].raw_production for j in range(indexes_variations[i],indexes_variations[i+1])]
            if debug : print("  variation "+str(i)+": ", variation)

            argpeak_variation = np.argmax(variation)
            #if debug : print("  arg peak: ", argpeak_variation)

            argascending_variation = max(argpeak_variation, 0)
            #if debug : print("  arg ascending: ", argascending_variation)

            start_ascending_variation = argpeak_variation - min(argascending_variation, decharge_duration)
            #if debug : print("  arg start ascending: ", start_ascending_variation)

            ascending_score = np.mean(variation[start_ascending_variation:argpeak_variation])
            #if debug : print("  score ascending: ", ascending_score)

            max_score = np.max(variation)
            #if debug : print("  score peak: ", max_score)

            score = max_score-ascending_score

            if debug :  print("     Is the variation peak ahead ? ", index_now < indexes_variations[i]+argpeak_variation)
            if index_now < indexes_variations[i]+argpeak_variation:
                if debug :  print("     Is the variation peak interesting ? ", not score < threshold)
                if score < threshold :
                    for j in range(indexes_variations[i],indexes_variations[i+1]):
                            if j > index_now:
                                usages[j].production = 0
                else :
                    for j in range(indexes_variations[i],indexes_variations[i+1]):
                            if j > index_now:
                                usages[j].production = usages[j].raw_production

                if debug : print("      filtered production after variation "+str(i)+": ", [usages[j].production for j in range(len(usages))])

    # filtering future
    indexes_variations = raw_variations(usages)
    removing = False
    for i in range(len(indexes_variations)-1):
        if removing:
            for j in range(indexes_variations[i], indexes_variations[i+1]):
                    usages[j].production = 0
        if debug : print("> ",indexes_variations[i], index_now + 1)
        if indexes_variations[i] > index_now + 1 :
            removing = True
    if debug : print("filtered production after removing future variations: ", [usages[j].production for j in range(len(usages))])

    # discrete scale
    data_scale = 15
    data_step = 1./data_scale
    for j in range(len(usages)):
        usages[j].production = int(usages[j].production/data_step) * data_step
    if debug : print("filtered production after discretization: ", [usages[j].production for j in range(len(usages))])

    #usages = [usages[j] for j in range(len(usages)) if ((usages [j].timestamp.hour >= min_hour) and (usages [j].timestamp.hour <= min_hour))]
    if debug : print("filtering(usages, now_frame, min_frame, max_frame): ", [usages[j].production for j in range(len(usages))])

    return usages

def init():
    now_frame = timezone.now() + datetime.timedelta(hours=2)
    min_frame = now_frame.replace(hour=0, minute=0, second=0, microsecond = 0)
    for timestamp in (min_frame + datetime.timedelta(hours=n) for n in range(24)):
        try :
            usage = EnergyUsage.objects.get(timestamp=timestamp)
        except :
            print("init :",timestamp)
            usage = EnergyUsage(timestamp=timestamp, raw_production=0, production=0, consumption=0)
            usage.save()

def run():
    init()
    now_frame = timezone.now() + datetime.timedelta(hours=2)
    min_frame = now_frame.replace(hour=0, minute=0, second=0, microsecond = 0)
    max_frame = now_frame.replace(hour=23, minute=0, second=0, microsecond = 0)
    epicesParser = EpicesParser('6bm-cRpuq5X3HwdphKU5x8lInv4')
    epicesParser.update()
    times = epicesParser.times
    productions = epicesParser.forecasts
    now_frame = timezone.now() + datetime.timedelta(hours=2)

    print("(now_frame.hour, it_frame.hour, raw_production)")
    for timestamp, production in zip(times, productions):
        print(now_frame.hour, timestamp.hour, float(production))
        try :
            usage = EnergyUsage.objects.get(timestamp=timestamp)
            usage.raw_production = float(production)
            usage.save()
        except :
            usage = EnergyUsage(timestamp=timestamp, raw_production=float(production), production=0, consumption=0)
            usage.save()

    min_frame = now_frame.replace(hour=8, minute=0, second=0, microsecond=0)
    max_frame = now_frame.replace(hour=17, minute=0, second=0, microsecond=0)
    usages = EnergyUsage.objects
    usages = usages.exclude(timestamp__lt=min_frame)
    usages = usages.exclude(timestamp__gt=max_frame)
    usages = usages.order_by('timestamp')
    if len(usages):
        usages = filtering(usages, now_frame.hour, min_frame.hour, max_frame.hour)
        for usage in usages:
            usage.save()

