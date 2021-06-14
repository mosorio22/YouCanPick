#you_can_pick.py
# Using the yelp business search API: https://www.yelp.com/developers/documentation/v3/business_search

import requests
import random
from pyzipcode import ZipCodeDatabase

def you_can_pick(zip_code):
	api_key = 'your key goes here'
	headers = {'Authorization': 'Bearer {}'.format(api_key)}

	search_api_url = 'https://api.yelp.com/v3/businesses/search'

	zcdb = ZipCodeDatabase()
	zipcode = zcdb[zip_code]
	city = zipcode.city
	state = zipcode.state
	location = city + ", " + state
	params = {'term': 'food', 'location': location}
	response = requests.get(search_api_url, headers=headers, params=params, timeout=5)
	eateries = response.json()["businesses"]
	random_restaurant = random.choice(list(eateries))['name']
	return random_restaurant

