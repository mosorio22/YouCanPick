# you_can_pick.py
# Using the yelp business search API: https://www.yelp.com/developers/documentation/v3/business_search

import requests
import random
from pyzipcode import ZipCodeDatabase
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

    zip_code = specs.get("zip-code")
    zcdb = ZipCodeDatabase()
    zcdb_metadata = zcdb[zip_code]

    # Get location
    city = zcdb_metadata.city
    state = zcdb_metadata.state
    location = city + ", " + state

    # Get category
    category = get_category(api_key, specs.get("category"))

    # Execute Yelp business search
    params = {'term': 'restaurant', 'open_now': True, 'location': location}
    price = specs.get("price")
    reservation = specs.get("reservation")

    if price:
        params["price"] = price
    if reservation:
        params["attributes"] = reservation
    if category:
        params["categories"] = category

    response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
    eateries = response.json()["businesses"]

    random_restaurant = random.choice(list(eateries))
    return random_restaurant
