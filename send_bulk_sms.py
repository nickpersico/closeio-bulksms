import sys
from collections import Counter
from _functions import get_internal_phone_number
from _functions import get_list_of_leads
from _functions import post_sms

API_KEY = sys.argv[1]
SEARCH_QUERY = sys.argv[2]
MESSAGE = sys.argv[3]

# Get the user's internal Close.io phone number to send SMS
internal_phone_number = get_internal_phone_number(API_KEY)

# Get the list of leads from the given search query
leads = get_list_of_leads(API_KEY, SEARCH_QUERY)

for lead in leads:

	# Retrieve the lead ID
	lead_id = lead['id']

	# Sends message to the first contact & first number on the lead only.
	contact_id = lead['contacts'][0]['id']
	contact_phone_number = lead['contacts'][0]['phones'][0]['phone']

	# Messages are set to the "outbox" status by default.
	# They will send immediately. For more status options, check here:
	# https://developer.close.io/#activities-create-an-sms-activity
	payload = {
		"status": "outbox",
		"text": MESSAGE,
		"local_phone": internal_phone_number,
		"remote_phone": contact_phone_number,
		"lead_id": lead_id,
		"contact_id": contact_id
	}

	# Sends the SMS, print the API response
	send_sms = post_sms(API_KEY, payload)
	print send_sms
