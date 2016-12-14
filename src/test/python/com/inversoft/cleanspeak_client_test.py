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


if __name__ == '__main__':
    unittest2.main()