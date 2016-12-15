import json

import datetime

from com.inversoft.cleanspeak_client import CleanSpeakClient


def current_time_millis():
    delta = datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)
    return delta.total_seconds() * 1000

#  You must supply your API key and URL here
client = CleanSpeakClient('your-api-key', 'https://your-cleanspeak-api.inversoft.io')

# Send a message to CleanSpeak to be moderated. This API requires that you create an Application and configure it with your filter rules. Once you
# have configured the Application, copy its id into the code below.
client_response = client.moderate({
    'content': {
        'applicationId': '<api-id-goes-here>',
        'createInstant': current_time_millis(),
        'location': 'some-place',
        'parts': [
            {
                'content': 'fuck off',
                'type': 'text'
            }
        ],
        'senderId': '<id-of-the-user-that-created-the-content>'
    }
})

if client_response.was_successful():
    print json.dumps(client_response.success_response)
else:
    print json.dumps(client_response.error_response)
