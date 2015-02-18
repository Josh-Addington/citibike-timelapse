import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citibike_viz_project.settings")

import django
django.setup()

from map.models import Station, Bike
import datetime

# CRON job to update bike table, run every 10 minutes

res = requests.get('http://www.citibikenyc.com/stations/json')
json_response = res.json()
station_info = json_response['stationBeanList']
# postgres needs 24 hour time, citibike supplies 12 w/ am/pm
execution_time = datetime.datetime.strptime(json_response['executionTime'], "%Y-%m-%d %I:%M:%S %p").strftime("%Y-%m-%d %H:%M:%S")


def add_bikes(json_file):
        for row in json_file:
                station_id = Station.objects.get(id=row['id'])
                b = Bike.objects.get_or_create(station=station_id,
                                               number_of_bikes=row['availableBikes'],
                                               time=execution_time)[0]
                print(b)

add_bikes(station_info)
