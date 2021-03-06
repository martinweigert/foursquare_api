import json, requests

# This script searches Foursquare at a given location, prints the results and stores them in a .txt file.
# Obtain your client id and client_secret at developer.foursquare.com.

client_id = # add your client_id here
client_secret = # add your client-secret here

global where
global what
where = "Stockholm, Sweden" # change for different location, e.g. "Berlin, Germany"
what = "burger" # change for different thing to surch for
limit = 5 # number of search results. change if needed.


def search(near,query,limit,client_id,client_secret):
    url = 'https://api.foursquare.com/v2/venues/search'

    params = dict(
        client_id=client_id,
        client_secret=client_secret,
        v='20170801',
        near=near,
        query=query,
        limit=limit
        )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    for i in range(limit):
        try:
            venue_id = data['response']['venues'][i]['id']
            get_venue_data_from_search(venue_id,client_id,client_secret)

        except:
            "finished"

get_venue_data_counter = [1]

def get_venue_data_from_search(venue_id,client_id,client_secret):

    url_venue = ('https://api.foursquare.com/v2/venues/%s' % venue_id)

    params = dict(
        client_id=client_id,
        client_secret=client_secret,
        v='20170801')

    resp_venue = requests.get(url=url_venue,params=params)
    data_venue = json.loads(resp_venue.text)

    print(" ")
    try:
        name = data_venue['response']['venue']['name']
        print("Name: %s" % name)
    except:
        name = "n/a"
        print("Name: %s" % name)
    try:
        address = data_venue['response']['venue']['location']['address']
        print("Address: %s" % address)
    except:
        address = "n/a"
        print("Address: %s" % address)
    try:
        city = data_venue['response']['venue']['location']['city']
        print("City: %s" % city)
    except:
        city = "n/a"
        print("City: %s" % city)
    try:
        country = data_venue['response']['venue']['location']['country']
        print("Country: %s" % country)
    except:
        country = "n/a"
        print("Country: %s" % country)
    try:
        rating = data_venue['response']['venue']['rating']
        print("Rating: %s" % rating)
    except:
        rating = "n/a"
        print("Rating: %s" % rating)
    try:
        checkins = data_venue['response']['venue']['stats']['checkinsCount']
        print("Checkins: %s" % checkins)
    except:
        checkins = "n/a"
        print("Checkins: %s" % checkins)
    try:
        tips = data_venue['response']['venue']['stats']['tipCount']
        print("Tips: %s" % tips)
    except:
        tips = "n/a"
        print("Tips: %s" % tips)
    try:
        url = data_venue['response']['venue']['shortUrl']
        print("URL: %s" % url)
    except:
        url = "n/a"
        print("URL: %s" % url)
    print("###")

    filename = ("%s_%s.txt" % (where,what))

    with open(filename,'a') as file:
        if get_venue_data_counter[0] == 1:
            firstrow = "name" + ";" + "address" + ";" + "city" + ";" + "country" + ";" + "rating" + ";" + "checkins" + ";" + "tips" + ";" + "url" + "\n"
            file.write(firstrow)
            get_venue_data_counter[0] += 1
        row = str(name) + ";" + str(address) + ";" + str(city) + ";" + str(country) + ";" + str(rating) + ";" + str(checkins) + ";" + str(tips) + ";" + str(url) + "\n"
        file.write(row)





search(where,what,limit,client_id,client_secret)
