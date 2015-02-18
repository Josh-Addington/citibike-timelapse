import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citibike_viz_project.settings")

import django
django.setup()

import csv
from map.models import Station, TripStart, TripEnd
from decimal import *
import datetime


getcontext().prec = 9


data_folder = 'data'
end_folder = 'trip_end'
start_folder = 'trip_start'
start_file_list = os.listdir(os.path.join(data_folder, start_folder))
# start_file_list = os.path.join(data_folder, os.listdir(os.path.join(data_folder, start_folder)))
end_file_list = os.listdir(os.path.join(data_folder, end_folder))


def populate():
    print(start_file_list, end_file_list)
    populate_stations(os.path.join(data_folder, 'stations.csv'))
    iter_over_files(start_file_list, os.path.join(data_folder, start_folder))
    iter_over_files(end_file_list, os.path.join(data_folder, end_folder))


def iter_over_files(list, folder):
        # fill Trips table
        for file in list:
            print(folder)
            if(folder == 'data/trip_start'):
                print('start')
                populate_trips(os.path.join(folder, file), 'start')
            elif(folder == 'data/trip_end'):
                populate_trips(os.path.join(folder, file), 'end')


def populate_stations(path):
        f = open(path, 'rt')
        try:
                reader = csv.DictReader(f)
                for row in reader:
                    add_station(
                        str(row['id']),
                        row['name'],
                        Decimal(row['latitude']),
                        Decimal(row['longitude'])
                    )

        finally:
                f.close()


def populate_trips(path, table):
        f = open(path, 'rt')
        print(path)
        try:
                reader = csv.DictReader(f)
                for row in reader:

                datetime.datetime.strptime("", "%m/%d/%Y %H:%M:%S,%f").strftime("%Y-%m-%d %H:%M:%S,%f")

                    if(table == 'start'):
                                add_tripStart(str(row['time']),
                                              row['station'])
                    elif(table == 'end'):
                                add_tripEnd(str(row['time']),
                                            row['station'])
        finally:
                f.close()


def add_station(id, name, lat, longi):
        s = Station.objects.get_or_create(id=id, name=name, latitude=lat, longitude=longi)[0]
        return s


def add_tripStart(time, station):
        print(time)
        station_id = Station.objects.get(id=station)
        t = TripStart.objects.get_or_create(station=station_id, time=time)[0]
        return t


def add_tripEnd(time, station):
        station_id = Station.objects.get(id=station)
        t = TripEnd.objects.get_or_create(station=station_id, time=time)[0]
        return t


if __name__ == '__main__':
        print("Starting population script")
        # iter_over_files(file_list)
        populate()
