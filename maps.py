import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDjnXIYsNbdsEK4jbt-1i_-lJ_YNRgZumw')

#Reverse geocoding
def find_address(latitude, longitude):
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))


