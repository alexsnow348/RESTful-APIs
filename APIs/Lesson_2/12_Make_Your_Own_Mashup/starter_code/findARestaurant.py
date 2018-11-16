from geocode import getGeocodeLocation
import json
import requests as rq

# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "KVPM5EQSUDNR4EAWRYYMQYTPJ34DZYJCTLV5CXDLAZQ1HVCV"
foursquare_client_secret = "5PA31GJ2UJ2SKM1I20MO4YYG02YSZCWZEI4IB0TZLRNEZUGC"


def findARestaurant(mealType, location):
    # 1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latitude, longitude = getGeocodeLocation(location)

    # 2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
    # HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id,
                                                                                                                       foursquare_client_secret,
                                                                                                                       latitude, longitude, mealType))

    h = rq.get(url)
    result = json.loads(h.text)
    # 3. Grab the first restaurant
    restaurant_name = result['response']['venues'][0]['name']
    venue_id = result['response']['venues'][0]['id']
    restaurant_address = result['response']['venues'][0]['location']['formattedAddress']

    restaurant_address = ','.join(str(e) for e in restaurant_address)
    print("Restaurant Name:", restaurant_name)
    print("Restaurant Address:", restaurant_address)

    # 4. Get a  300x300 picture of the restaurant using the venue_id
    # (you can change this by altering the 300x300 value in the URL
    # or replacing it with 'orginal' to get the original picture
    url_photo = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' %
                 (venue_id, foursquare_client_id, foursquare_client_secret))

    h = rq.get(url_photo)
    result = json.loads(h.text)
    if len(result['response']['photos']['items']) > 0:
        prefix = result['response']['photos']['items'][0]['prefix']
        suffix = result['response']['photos']['items'][0]['suffix']
        imageURL = prefix + "300x300" + suffix
    else:
        imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"

    print("Image: ", imageURL)


if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")

    # findARestaurant("Tacos", "Jakarta, Indonesia")
    # findARestaurant("Tapas", "Maputo, Mozambique")
    # findARestaurant("Falafel", "Cairo, Egypt")
    # findARestaurant("Spaghetti", "New Delhi, India")
    # findARestaurant("Cappuccino", "Geneva, Switzerland")
    # findARestaurant("Sushi", "Los Angeles, California")
    # findARestaurant("Steak", "La Paz, Bolivia")
    # findARestaurant("Gyros", "Sydney Australia")
