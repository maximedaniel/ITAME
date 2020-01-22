import pandas as pd

FILENAME_RAW_LAPTOP = './data/laptop_raw.csv'
FILENAME_RAW_FORECAST = './data/forecast_raw.csv'
FILENAME_FILTERED_LAPTOP = './data/laptop_filtered.csv'
FILENAME_FILTERED_FORECAST = './data/forecast_filtered.csv'
HOUR_MIN = 8
HOUR_MAX = 17

MAX_POWER = 5000 #W

# Filtering raw laptop data
dfLaptop = pd.read_csv(FILENAME_RAW_LAPTOP)
dfLaptop['timestamp'] =  pd.to_datetime(dfLaptop['timestamp'])
#dfLaptop = dfLaptop[(dfLaptop['timestamp'].dt.hour >= HOUR_MIN) & (dfLaptop['timestamp'].dt.hour <= HOUR_MAX)]
dfLaptop = dfLaptop[(dfLaptop['near'] != 0)]
dfLaptop = dfLaptop.replace({'plugged': {0 : "battery", 1 : "battery_sector"}})
dfLaptop = dfLaptop[['timestamp', 'username', 'estimatedChargeRemaining', 'plugged']]
dfLaptop = dfLaptop.rename(columns={"estimatedChargeRemaining": "storage", "plugged":"usage"})
dfLaptop.to_csv(FILENAME_FILTERED_LAPTOP, index = None, header=True) 

# Filtering raw forecast data
dfForecast = pd.read_csv(FILENAME_RAW_FORECAST)
dfForecast['timestamp'] =  pd.to_datetime(dfForecast['timestamp'])
#dfForecast = dfForecast[(dfForecast['timestamp'].dt.hour >= HOUR_MIN) & (dfForecast['timestamp'].dt.hour <= HOUR_MAX)]
dfForecast = dfForecast[['timestamp', 'production']]
dfForecast.to_csv(FILENAME_FILTERED_FORECAST, index = None, header=True) 
