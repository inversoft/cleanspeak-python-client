#
# Copyright (c) 2016, Inversoft Inc., All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#

import json

import unittest2

import uuid

from com.inversoft.cleanspeak_client import CleanSpeakClient


class ClientTest(unittest2.TestCase):
    def setUp(self):
        self.client = CleanSpeakClient('1f9e348a-61ab-4f53-8a73-3df91c0b5d76', 'http://localhost:8001')

    def runTest(self):
        pass

    def test_filter(self):
        cr = self.client.filter({
            'content': 'fuck you asshole'
        })

        self.assertEqual(cr.status, 200)
        self.assertEqual(cr.success_response['matches'][0]['start'], 0)
        self.assertEqual(cr.success_response['matches'][0]['length'], 4)
        self.assertEqual(cr.success_response['matches'][0]['matched'], 'fuck')
        self.assertEqual(cr.success_response['matches'][0]['root'], 'fuck')
        self.assertEqual(cr.success_response['matches'][0]['severity'], 'severe')

    def test_moderate_then_flag(self):
        # First moderate (and create)
        id = uuid.uuid4()
        sender_id = uuid.uuid4()
        reporter_id = uuid.uuid4()
        cr = self.client.moderate({
            'content': {
                'applicationId': '4305999d-e3c4-44dc-8955-d2b21b655806',
                'createInstant': 42,
                'parts': [{
                    'type': 'text',
                    'name': 'content',
                    'content': 'Fuck off'
                }],
                'senderId': str(sender_id)
            }
        }, id)

        self.assertEqual(cr.status, 200)
        self.assertEqual(cr.success_response['contentAction'], 'reject')

        # Now flag
        cr = self.client.flag({
            'flag': {
                'comment': 'testing 123',
                'createInstant': 42,
                'reporterId': str(reporter_id)
            }
        }, id)

        self.assertEqual(cr.status, 200)

    #
    # def print_json(self, parsed_json):
    #     print json.dumps(parsed_json, indent=2, sort_keys=True)
    #
    # def test_retrieve_applications(self):
    #     client_response = self.client.retrieve_applications()
    #     self.assertEqual(client_response.status, 200)
    #     self.assertEqual(len(client_response.success_response['applications']), 3)
    #
    # def test_create_user_retrieve_user(self):
    #     # Check if the user already exists.
    #     get_user_response = self.client.retrieve_user_by_email('art@vandaleyindustries.com')
    #     if get_user_response.status is 200:
    #         delete_user_response = self.client.delete_user(get_user_response.success_response['user']['id'])
    #         self.assertEqual(delete_user_response.status, 200, delete_user_response.error_response)
    #     else:
    #         self.assertEqual(get_user_response.status, 404, get_user_response.error_response)
    #
    #     # Create a new registration for this user.
    #     user_request = {
    #         'sendSetPasswordEmail': False,
    #         'skipVerification': True,
    #         'user': {
    #             'email': 'art@vandaleyindustries.com',
    #             'password': 'password'
    #         }
    #     }
    #     create_user_response = self.client.create_user(None, user_request)
    #     self.assertEqual(create_user_response.status, 200, create_user_response.error_response)
    #
    #     # Retrieve the user
    #     user_id = create_user_response.success_response['user']['id']
    #     get_user_response = self.client.retrieve_user(user_id)
    #     self.assertEqual(get_user_response.status, 200)
    #     self.assertIsNotNone(get_user_response.success_response)
    #     self.assertIsNone(get_user_response.error_response)
    #     self.assertEquals(get_user_response.success_response['user']['email'], 'art@vandaleyindustries.com')
    #     self.assertFalse('password' in get_user_response.success_response['user'])
    #     self.assertFalse('salt' in get_user_response.success_response['user'])
    #
    # def test_retrieve_user_missing(self):
    #     user_id = uuid.uuid4()
    #     client_response = self.client.retrieve_user(user_id)
    #     self.assertEqual(client_response.status, 404)
    #     self.assertEqual(client_response.success_response, None)
    #     self.assertIsNotNone(client_response.error_response)


if __name__ == '__main__':
    unittest2.main()