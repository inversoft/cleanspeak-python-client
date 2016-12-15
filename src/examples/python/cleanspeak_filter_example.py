import json

import datetime

from com.inversoft.cleanspeak_client import CleanSpeakClient


#  You must supply your API key and URL here
client = CleanSpeakClient('your-api-key', 'https://your-cleanspeak-api.inversoft.io')

# Send a message to CleanSpeak to be filtered
client_response = client.filter({
    'content': 'fuck off'
})

if client_response.was_successful():
    print client_response.success_response.json()
