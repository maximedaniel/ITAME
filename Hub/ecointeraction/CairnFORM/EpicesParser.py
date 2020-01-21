import requests
from dateutil import parser

class EpicesParser:
	def __init__(self, token):
		self.token = token
		self.last_update = None
		self.id = None
		self.name = None
		self.max_wh = None
		self.times = []
		self.forecasts = []
		self.update()

	def init(self):
		r = requests.get('http://api.epices-energie.fr/v1/sites_list', headers={'Authorization': ('Token token='+self.token)})
		if r.status_code != 200:
			return
		r = r.json()
		self.last_update = parser.parse(r['request_timestamps']['received_at'])
		self.id = r['sites_list'][0]['id']
		self.name = r['sites_list'][0]['name']
		self.max_wh = r['sites_list'][0]['peak_power_kwp']*1000.
		self.times = []
		self.forecasts = []
		#print(self.last_update, self.id, self.name, self.max_wh)

	def forecast(self):
		r = requests.get('http://api.epices-energie.fr/v1/site_hourly_production?site_id='+str(self.id), headers={'Authorization': ('Token token='+self.token)})
		if r.status_code != 200:
			return
		r = r.json()
		predictions = r['site_hourly_production']['hourly_productions']
		for prediction in predictions:
			self.times.append(parser.parse(prediction['utc_timestamps']))
			self.forecasts.append(prediction['satellite_reference_in_wh']/self.max_wh)
		#print(self.times)
		#print(self.forecasts)

	def update(self):
		self.init()
		self.forecast()