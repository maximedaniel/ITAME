import requests, zipfile, io, os, time
import pandas as pd
import numpy as np
import datetime
from threading import Timer
import random
import sys
from django.utils import timezone

def processProductionForecast(tomorrow):
	process_url = 'http://itame.estia.fr/production/processForecast/'
	r = requests.get(process_url)
	print(r.content)

def postProductionForecast(tomorrow):
	#  extract PrevisionProduction.xlsx from the zip file downloaded from http://clients.rte-france.com
	url_global_production_zip = 'http://clients.rte-france.com/servlets/PrevProdServlet?jour='+tomorrow.strftime('%d/%m/%Y');
	print("download zip file from ",url_global_production_zip,"...")
	r = requests.get(url_global_production_zip)
	z = zipfile.ZipFile(io.BytesIO(r.content))
	z.extractall()
	print("unzip file PrevisionProduction.zip...")
	prevision_production_csv = pd.read_csv('PrevisionProduction.xls', sep='\t', encoding = "latin1")
	print("Parsing PrevisionProduction.xls...")
	prevision_production_dimension = prevision_production_csv.shape
	steps = prevision_production_dimension[0]-1
	for i in range(prevision_production_dimension[0]-1):# do not iterate on the last row
		hour_splitted = prevision_production_csv.ix[i][1].split(':');
		timestamp = tomorrow.replace(hour=int(hour_splitted[0]),minute=int(hour_splitted[1]))
		grey_power = prevision_production_csv.ix[i][2]
		green_power = prevision_production_csv.ix[i][3]
		green_rate=green_power/(grey_power+green_power)
		post_url = 'http://itame.estia.fr/production/postForecast/'
		post_url = post_url+timestamp.strftime('%Y/%m/%d/%H/%M')+'/'+str(int(grey_power))+'/'+str(int(green_power))+'/'+str(green_rate)+'/'
		#print("saving ", post_url,"...")
		r = requests.get(post_url)
		#print(r.content)
		#time.sleep(random.random())
		#print('\r[{0}] {1}%'.format('#'*int(((i/steps)/10)), (i/steps)))
	print("parsing complete.")
	processProductionForecast(tomorrow)


today=datetime.datetime.now()
postProductionForecast(today)