#you_can_pick.py
# Using the yelp business search API: https://www.yelp.com/developers/documentation/v3/business_search

import requests
import random
from pyzipcode import ZipCodeDatabase

def you_can_pick(specs):
	api_key = 'api key goes here'
	headers = {'Authorization': 'Bearer {}'.format(api_key)}

	search_api_url = 'https://api.yelp.com/v3/businesses/search'

	zip_code = specs.get("zip-code")
	zcdb = ZipCodeDatabase()
	zipcode = zcdb[zip_code]
	city = zipcode.city
	state = zipcode.state
	location = city + ", " + state
	params = {'term': 'restaurant', 'open_now': True, 'location': location}
	price = specs.get("price")
	reservation = specs.get("reservation")
	if price != "":
		params["price"] = price
	if reservation != "":
		params["attributes"] = reservation
	response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
	eateries = response.json()["businesses"]
	random_restaurant = random.choice(list(eateries))
	print(random_restaurant)
	return random_restaurant

