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

import requests

class CleanSpeakClient(object):
    """The CleanSpeakClient provides easy access to the CleanSpeak API.

    Attributes:
        api_key: A string representing the API used to authenticate the API call to CleanSpeak
        base_url: A string representing the URL use to access CleanSpeak WebService (i.e. https://foo-cleanspeak-api.inversoft.io)

    """

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def create_user(self, user_id, user_request):
        return self.start().uri('/api/user').url_segment(user_id).request(user_request).post().go()

    def delete_user(self, user_id):
        return self.start().uri('/api/user').url_segment(user_id).url_parameter('hardDelete', 'true').delete().go()

    def login(self, login_request):
        return self.start().uri('/api/login').request(login_request).post().go()

    def retrieve_applications(self):
        """Retrieves all of the applications."""
        return self.start().uri('/api/application').get().go()

    def retrieve_user(self, user_id):
        """Retrieves the user for the given id.

        :type user_id: uuid The user's unique id.
        """
        return self.start().uri('/api/user').url_segment(user_id).get().go()

    def retrieve_user_by_email(self, email):
        """Retrieves the user for the given email.

        :type email: string The email of the user.
        """
        return self.start().uri('/api/user').url_parameter('email', email).get().go()

    def start(self):
        return RESTClient() \
            .authorization(self.api_key) \
            .url(self.base_url)

class RESTClient(object):
    """The RestClient used to build API calls to CleanSpeak.

    Attributes:
        _headers: The headers
        _method: The method
        _request: The request body
        _url: The url

    """

    def __init__(self):
        self._headers = {}
        self._method = None
        self._parameters = {}
        self._request = None
        self._url = None

    def authorization(self, key):
        self._headers['Authorization'] = key
        return self

    def content_type(self, content_type):
        self._headers['Content-Type'] = content_type
        return self

    def delete(self):
        self._method = 'DELETE'
        return self

    def get(self):
        self._method = 'GET'
        return self

    def go(self):
        if self._method is 'DELETE':
            return ClientResponse(
                requests.delete(self._url, headers=self._headers, params=self._parameters))
        elif self._method is 'GET':
            return ClientResponse(
                requests.get(self._url, headers=self._headers, params=self._parameters))
        elif self._method is 'POST':
            return ClientResponse(
                    requests.post(self._url, data=None, json=self._request, headers=self._headers,
                                  params=self._parameters))
        else:
            raise ValueError('The HTTP method must be set to POST, PUT, GET or DELETE prior to calling go()')

    def post(self):
        self._method = 'POST'
        return self

    def put(self):
        self._method = 'PUT'
        return self

    def request(self, request):
        self._request = request
        return self

    def uri(self, uri):
        if self._url is None:
            return self

        if self._url.endswith('/') and uri.startswith('/'):
            self._url += uri[:1]
        else:
            self._url += uri

        return self

    def url(self, url):
        self._url = url
        return self

    def url_parameter(self, name, value):
        if value is None:
            return self

        values = self._parameters.get(name)
        if values is None:
            values = []
            self._parameters[name] = values

        values.append(value)
        return self

    def url_segment(self, segment):
        if segment is not None:
            if not self._url.endswith('/'):
                self._url += '/'

            self._url += segment if type(segment) is str else str(segment)

        return self


def to_json(obj):
    return json.dumps(obj, default=default_json_handler)


def to_pretty_json(obj):
    return json.dumps(obj, default=default_json_handler,
                      sort_keys=True, indent=4)


def default_json_handler(obj):
    if isinstance(obj, set):
        return list(obj)

    if isinstance(obj, bool):
        return "foo" if True else "bar"

    if obj is 'null':
        return 'foo'

    return obj.__dict__


class ClientResponse(object):
    """The ClientResponse returned from the the CleanSpeak API.

    Attributes:
        error_response:
        exception:
        response: The full response object
        success_response:
        status:
    """

    def __init__(self, response):
        self.error_response = None
        self.exception = None
        self.response = response
        self.success_response = None
        self.status = response.status_code

        if self.status < 200 or self.status > 299:
            if self.response.content is not None and self.status is not 404:
                if self.status is 400:
                    self.error_response = self.response.json()
                else:
                    self.error_response = self.response
        else:
            try:
                self.success_response = self.response.json()
            except ValueError:
                self.success_response = None

    def was_successful(self):
        return 200 <= self.status <= 299 and self.exception is None