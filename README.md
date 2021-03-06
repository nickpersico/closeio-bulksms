# Close.io - Send Bulk SMS
Send SMS messages in bulk using your Close.io phone number

### How It Works

The script will send an SMS to the first contact on a list of leads via a Close.io search query. The messages are sent via your Close.io phone number.

### Setup

1. Clone the repository.
1. In your Terminal, navigate to the folder: `cd /path/to/closeio-bulksms`.
1. Create a virtual environment with [virtualenv](https://virtualenv.pypa.io/en/stable/): `virtualenv venv`
1. Activate it: `source venv/bin/activate`
1. Install the requirements needed to run the script: `pip install -r requirements.txt`
1. Run the script: `python send_bulk_sms.py 'YOUR API KEY' 'CLOSE.IO SEARCH QUERY' 'YOUR SMS MESSAGE'`

The script should find the leads in the search query and send an SMS to the first contact (and first phone number) on each lead. The script will output the raw response from the Close.io API.

### Example

Send an SMS to 5 leads that have the lead status as "potential":

`python send_bulk_sms.py 'YOUR API KEY' 'status:confirmed limit:5' 'This is a test message!'`

### Notes

- The default `status` of each SMS is `outbox`. That will send the SMS immediately from your internal Close.io phone number.
- Any errors with delivering the SMS will show up on the lead in Close.io.
- SMS messages will be sent from your internal Close.io phone number. It must be SMS-enabled and a US/Canada number.
- Any SMS that are sent will subtract from your free credits or be charged to your Close.io invoice. Here's more info about [SMS billing in Close.io](https://help.close.io/customer/en/portal/articles/2677062-how-does-sms-billing-work-).

Questions? Email [nick@close.io](mailto:nick@close.io) or send a [Tweet](https://www.twitter.com/nickpersico).