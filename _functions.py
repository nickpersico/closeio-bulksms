from closeio_api import Client
import urllib


# Get list of leads from search query
def get_list_of_leads(api_key, search_query):

	api = Client(api_key)

	has_more = True
	offset = 0
	leads = []

	while has_more:

		lead_results = api.get(
			'lead',
			params={
		    	'query': search_query,
		    	'_skip': offset,
		    	'limit': 100
			}
		)

		lead_data = lead_results['data']

		for l in lead_data:
			leads.append(l)

		offset += len(lead_data)
		has_more = lead_results['has_more']

	return leads


# Post an SMS message
def post_sms(api_key, payload):

	api = Client(api_key)

	message = api.post(
		'activity/sms',
		data=payload
	)

	return message


# Retrieve internal phone number for Close.io user
def get_internal_phone_number(api_key):

	api = Client(api_key)

	user_response = api.get('me')
	phone_number = user_response['phone_numbers'][0]['number']

	return phone_number




