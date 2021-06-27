# you_can_pick.py
# Using the yelp business search API: https://www.yelp.com/developers/documentation/v3/business_search

import requests
import random
import json
from fuzzywuzzy import process
import os.path


def get_api_key():
    with open(os.path.dirname(__file__) + '/../resources/api.json', 'r') as fp:
        j = json.load(fp)
        api_key = j['api_key']

    return api_key


def get_category(api_key, search_keyword):
    if not search_keyword:
        return None

    # Get all Yelp categories
    with open(os.path.dirname(__file__) + '/../resources/categories.json', 'r') as fp:
        j = json.load(fp)
        categories = []
        for i in range(0, len(list(j))):
            if "restaurants" in j[i]["parents"]:
                categories.append(j[i]["alias"])

    # Fuzzy match on search keyword
    best_match = process.extractOne(search_keyword, [x for x in categories])[0]

    return best_match


def you_can_pick(specs):
    api_key = get_api_key()
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    search_api_url = 'https://api.yelp.com/v3/businesses/search'


    # Get location
    location = specs.get("zip-code")
    address = specs.get("address")
    city = specs.get("city")
    state = specs.get("state")

    if state:
        location = state + " "  + location
    if city:
        location = city + ", " + location
    if address:
        location = address +", " + location


    # Execute Yelp business search
    params = {'term': 'restaurant', 'open_now': True, 'location': location}

    distance = specs.get("distance")
    reservation = specs.get("reservation")
    category = get_category(api_key, specs.get("category"))

    #create price
    min_price = specs.get("min-price")
    max_price = specs.get("max-price")
    if min_price and max_price:
        #create comma separated string of prices
        price = list(range(int(min_price), int(max_price) + 1))
        price = ", ".join(map(str, price))
    else:
        price = "1, 2, 3, 4"

    if reservation:
        params["attributes"] = reservation
    if distance:
        #convert miles to meters
        distance = int(distance) * 1609
        params["radius"] = distance
    if category:
        params["categories"] = category
    if price:
        params["price"] = price

    response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    eateries = response.json()["businesses"]

    random_restaurant = random.choice(list(eateries))
    return random_restaurant
