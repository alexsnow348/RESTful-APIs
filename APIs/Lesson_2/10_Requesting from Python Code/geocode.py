import requests as rq
import json


def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    google_api_key = "AIzaSyCHt4ZQk9uQPxrsd2G5JZAfjHpHUb4W-mA"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %
           (locationString, google_api_key))

    h = rq.get(url)
    result = json.loads(h.text)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)


print(getGeocodeLocation("Cyberjaya Malaysia"))
