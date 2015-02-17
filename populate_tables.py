import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citibike_viz_project.settings")

import django
django.setup()

import csv
from map.models import Station, TripStart, TripEnd
from decimal import *
import requests
import json


getcontext().prec = 9


folder = 'data'
file_list = os.listdir(folder)

# Tried to create a trips array in iter_over_file(),
# pass it to get_info() and have get_info append each trip
# to the array. That took up way too much RAM.
json_response = requests.get('http://www.citibikenyc.com/stations/json')
response = json_response.json()
station_amount = len(response['stationBeanList'])


def iter_over_files(list):
        # Create a dict of stations, to prevent duplicates
        # stations = {}

        # fill Stations table first
        # Trips table depends on Stations table
        # for file in list:
        #       stations.update(get_stations(os.path.join(folder, file), stations))
        #        if(len(stations) == station_amount):
        #                break
        # Populate Stations table using stations dict
        # populate_stations(stations)

        # fill Trips table
        for file in list:
                populate_trips(os.path.join(folder, file))


def get_stations(path, stations):
        f = open(path, 'rt')
        something = {}
        try:
                reader = csv.DictReader(f)
                for row in reader:
                        if row['start station id'] not in stations:
                                something[str(row['start station id'])] = {
                                    'name': row['start station name'],
                                    'latitude': Decimal(row['start station latitude']),
                                    'longitude': Decimal(row['start station longitude'])}
                        elif row['end station id'] not in stations:
                                something[str(row['end station id'])] = {
                                    'name': row['end station name'],
                                    'latitude': Decimal(row['end station latitude']),
                                    'longitude': Decimal(row['end station longitude'])}

                        # trips.append({'start_station': row['start station id'], 'stop station': row['end station id'], 'start_time': row['starttime'], 'stop_time': row['stoptime']})
        finally:
                f.close()
        print(len(stations))
        return something


def populate_stations(stations):
        print(len(stations))
        for key in stations:
                add_station(key,
                            stations[key]['name'],
                            stations[key]['latitude'],
                            stations[key]['longitude'])


def populate_trips(path):
        # for line in trips:
        #         add_trip(row['start station id'],
        #                  row['end station id'],
        #                  row['starttime'],
        #                  row['stoptime'])
        f = open(path, 'rt')

        try:
                reader = csv.DictReader(f)
                for row in reader:
                                add_tripOut(row['start station id'],
                                            row['starttime'])
                                add_tripIn(row['end station id'],
                                           row['stoptime'])
        finally:
                f.close()


def add_station(id, name, lat, longi):
        s = Station.objects.get_or_create(id=id, name=name, latitude=lat, longitude=longi)[0]
        return s


def add_tripOut(station, time):
        station_id = Station.objects.get(id=station)
        t = TripStart.objects.get_or_create(station=station_id, time=time)[0]
        return t


def add_tripIn(station, time):
        station_id = Station.objects.get(id=station)
        t = TripEnd.objects.get_or_create(station=station_id, time=time)[0]
        return t


if __name__ == '__main__':
        print("Starting population script")
        iter_over_files(file_list)
