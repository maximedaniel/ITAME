import requests
from datetime import datetime
import pandas as pd
import json
# Global variables
URL_LAPTOP = 'http://itame.pythonanywhere.com/CairnFORM/getLaptopFromTo/'
URL_FORECAST = 'http://itame.pythonanywhere.com/CairnFORM/getEnergyUsageFromTo/'
FROM = datetime.strptime('20/01/2020 08:00:00', '%d/%m/%Y %H:%M:%S')
TO = datetime.strptime('20/01/2020 18:00:00', '%d/%m/%Y %H:%M:%S')
FILENAME_RAW_LAPTOP = './data/laptop_raw.csv'
FILENAME_RAW_FORECAST = './data/forecast_raw.csv'
DEBUG = True

# Acquire raw laptop data
print('Requesting LAPTOP from ['+ FROM.ctime() + '] to ['+ TO.ctime() +'] at ['+URL_LAPTOP+']...') if DEBUG else 0
r = requests.get(
    URL_LAPTOP + str(FROM.year) + '/' + str(FROM.month) + '/' + str(FROM.day) + '/'+ str(FROM.hour) + '/'+ str(FROM.minute) + '/'+ str(FROM.second)
    + '/' + str(TO.year) + '/' + str(TO.month) + '/' + str(TO.day) + '/'+ str(TO.hour) + '/'+ str(TO.minute) + '/'+ str(TO.second))
print('Succeed!' if r.status_code == 200 else 'Failed!') if DEBUG else 0
exit(1) if r.status_code != 200 else 0
print('Json Parsing...')
try:
    rawJson = json.loads(r.content)
    ansJson = [ item['fields'] for item in rawJson]
    for i in range(len(ansJson)):
        ansJson[i]['timestamp'] = rawJson[i]['pk']
    print('Succeed!')
    print('DataFrame Parsing...')
    ansDf = pd.DataFrame(ansJson)
    print('Succeed!')
    print('CSV exporting...')
    ansDf.to_csv (FILENAME_RAW_LAPTOP, index = None, header=True) 
    print('Succeed!')
except Exception as e:
    print('Failed!', e)

# Acquire raw forecast data
print('Requesting FORECAST from ['+ FROM.ctime() + '] to ['+ TO.ctime() +'] at ['+URL_FORECAST+']...') if DEBUG else 0
r = requests.get(
    URL_FORECAST + str(FROM.year) + '/' + str(FROM.month) + '/' + str(FROM.day) + '/'+ str(FROM.hour) + '/'+ str(FROM.minute) + '/'+ str(FROM.second)
    + '/' + str(TO.year) + '/' + str(TO.month) + '/' + str(TO.day) + '/'+ str(TO.hour) + '/'+ str(TO.minute) + '/'+ str(TO.second))
print('Succeed!' if r.status_code == 200 else 'Failed!') if DEBUG else 0
exit(1) if r.status_code != 200 else 0
print('Json Parsing...')
try:
    ansJson = [item['fields'] for item in json.loads(r.content)]
    print('Succeed!')
    print('DataFrame Parsing...')
    ansDf = pd.DataFrame(ansJson)
    print('Succeed!')
    print('CSV exporting...')
    ansDf.to_csv (FILENAME_RAW_FORECAST, index = None, header=True) 
    print('Succeed!')
except Exception as e:
    print('Failed!', e)

