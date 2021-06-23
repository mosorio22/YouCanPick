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

def get_restaurant_categories():
    with open(os.path.dirname(__file__) + '/../resources/categories.json', 'r') as fp:
        j = json.load(fp)
        restaurant_categories = []
        for i in range(0, len(list(j))):
            if "restaurants" in j[i]["parents"]:
                restaurant_categories.append(j[i]["alias"])

    return restaurant_categories


def get_category(api_key, search_keyword):
    if not search_keyword:
        return None

    # Get all Yelp categories
    request_url = 'https://api.yelp.com/v3/categories'
    headers = {'Authorization': 'Bearer {}'.format(api_key)}
    # params = {'locale': 'en_US'}
    params = {}
    response = requests.get(request_url, headers=headers, params=params, timeout=5)
    response_body = response.json()

    # Get relevant Yelp categories
    target = ['food', 'restaurants']
    categories = []
    while target:
        r = [x for x in response_body['categories'] if any(y in x['parent_aliases'] for y in target)]
        categories.extend([(x['title'], x['alias']) for x in r])
        # Get subcategories
        target = [x['alias'] for x in r]

    # Fuzzy match on search keyword
    best_match = process.extractOne(search_keyword, [x[0] for x in categories])[0]
    best_match_alias = [x[1] for x in categories if x[0] == best_match][0]

    return best_match_alias


def you_can_pick(specs):
    get_restaurant_categories()
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
    if not category:
        eateries = response.json()["businesses"]
    else:
        # Only return eateries with user-specified category
        eateries = [x for x in response.json()["businesses"] if
                    any(category in y['alias'] for y in x['categories'])]

    random_restaurant = random.choice(list(eateries))
    return random_restaurant
