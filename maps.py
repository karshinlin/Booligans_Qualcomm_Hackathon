import googlemaps
from datetime import datetime
from decimal import Decimal
import requests
import json
from flask import request

gmaps = googlemaps.Client(key='AIzaSyDjnXIYsNbdsEK4jbt-1i_-lJ_YNRgZumw')

#Reverse geocoding
def find_address(latitude, longitude):
    reverse_geocode_result = gmaps.reverse_geocode((Decimal(latitude), Decimal(longitude)))

def find_distance(originLat, originLong, destLat, destLong):
    data = {'temperature':'24.3'}
    data_json = json.dumps(data)
    payload = {'units' : 'imperial','origins': originLat + ',' + originLong, 'destinations': destLat + ',' + destLong, 'apikey': 'AIzaSyDjnXIYsNbdsEK4jbt-1i_-lJ_YNRgZumw'}
    r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+ originLat + ',' + originLong + '&destinations=' + destLat + ',' + destLong +'&key=AIzaSyDjnXIYsNbdsEK4jbt-1i_-lJ_YNRgZumw')
    distance = int(r.json()['rows'][0]['elements'][0]['distance']['text'].split(' ')[0])
    print(distance)
    #print(r['rows']['elements']['distance']['value'])
    return distance
#https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=32.8941450,-117.1958245&destinations=32.8941451,-117.1958246&key=AIzaSyDjnXIYsNbdsEK4jbt-1i_-lJ_YNRgZumw
