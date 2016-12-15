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

import requests


class CleanSpeakClient:
    """The CleanSpeakClient provides easy access to the CleanSpeak API.

    Attributes:
        api_key: A string representing the API used to authenticate the API call to CleanSpeak
        base_url: A string representing the URL use to access CleanSpeak WebService (i.e. https://foo-cleanspeak-api.inversoft.io)

    """
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def filter(self, filter_request):
        """Calls CleanSpeak to filter content. This calls CleanSpeak's /content/item/filter end-point.

        :parameter filter_request: The filter request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type filter_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/item/filter').request(filter_request).post().go()

    def flag(self, content_id, flag_request):
        """Calls CleanSpeak to indicate that a user has flagged another user's content (also known as reporting and often used to allow users to
        report content/chat from other users). This calls CleanSpeak's /content/item/flag end-point.

        :parameter content_id: The id of the piece of content that is being flagged (see the docs for more information).
        :parameter flag_request: The flag request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type content_id: uuid
        :type flag_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/item/flag').url_segment(content_id).request(flag_request).post().go()

    def moderate(self, content_id, moderate_request):
        """Calls CleanSpeak to moderate a piece of content according to the Application rules defined via the Management Interface. This calls
        CleanSpeak's /content/item/moderate end-point.

        :parameter content_id: (Optional) The id of the piece of content. This is only valid for persistent content Applications (see the docs for more information)
        :parameter moderate_request: The moderate request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type content_id: uuid
        :type moderate_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/item/moderate').url_segment(content_id).request(moderate_request).post().go()

    def moderate_update(self, content_id, moderate_request):
        """Calls CleanSpeak to update and re-moderate a piece of content that was updated externally by the user or a moderator. This re-moderates the
        content according to the Application rules defined via the Management Interface. This calls CleanSpeak's /content/item/moderate end-point.

        :parameter content_id: The id of the piece of content. This is only valid for persistent content Applications (see the docs for more information)
        :parameter moderate_request: The moderate request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type content_id: uuid
        :type moderate_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/item/moderate').url_segment(content_id).request(moderate_request).put().go()

    def action_user(self, user_id, action_request):
        """Calls CleanSpeak to notify it that a user was actioned outside of the CleanSpeak Management Interface. This calls CleanSpeak's
        /content/user/action end-point.

        :parameter user_id: The id of the user that is being actioned (see the docs for more information).
        :parameter action_request: The action request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type user_id: uuid
        :type action_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/user/action').url_segment(user_id).request(action_request).post().go()

    def flag_user(self, user_id, flag_request):
        """Calls CleanSpeak to indicate that a user has flagged another user for some type of inappropriate behavior. This calls CleanSpeak's
        /content/user/flag end-point.

        :parameter user_id: The id of the user that is being flagged (see the docs for more information).
        :parameter flag_request: The flag request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type user_id: uuid
        :type flag_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/user/flag').url_segment(user_id).request(flag_request).post().go()

    def delete_all_user_content(self, user_id):
        """Calls CleanSpeak to delete all of the content generated by a single user. This is helpful for COPPA compliance. This calls CleanSpeak's
        /content/item end-point.

        :parameter user_id: The id of the user whose content should be deleted (see the docs for more information).
        :type user_id: uuid
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/item').url_segment(user_id).delete().go()

    def create_user(self, user_id, user_request):
        """Calls CleanSpeak to create a user that will generate content (or already has). This stores the user details in CleanSpeak so that they are
        available in the Management Interface. This calls CleanSpeak's /content/user end-point.

        :parameter user_id: The id of the user being created (see the docs for more information).
        :parameter user_request: The user request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type user_id: uuid
        :type user_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/user').url_segment(user_id).request(user_request).post().go()

    def retrieve_user(self, user_id):
        """Calls CleanSpeak to retrieve a user. This calls CleanSpeak's /content/user end-point.

        :parameter user_id: The id of the user being retrieved (see the docs for more information).
        :type user_id: uuid
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/user').url_segment(user_id).get().go()

    def update_user(self, user_id, user_request):
        """Calls CleanSpeak to update a user that was previously created. This updates the user details in CleanSpeak so that they are
        available in the Management Interface. This calls CleanSpeak's /content/user end-point.

        :parameter user_id: The id of the user being updated (see the docs for more information).
        :parameter user_request: The user request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type user_id: uuid
        :type user_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/user').url_segment(user_id).request(user_request).put().go()

    def deleted_user(self, user_id):
        """Calls CleanSpeak to delete a user. This calls CleanSpeak's /content/user end-point.

        :parameter user_id: The id of the user being deleted (see the docs for more information).
        :type user_id: uuid
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/content/user').url_segment(user_id).delete().go()

    def retrieve_whitelist(self):
        """Calls CleanSpeak to retrieve the entire whitelist filter configuration. This is useful if your want to use a suggestion interface that
        needs a set of words. This calls CleanSpeak's /filter/whitelist end-point.

        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/filter/whitelist').get().go()

    def create_application(self, application_id, application_request):
        """Calls CleanSpeak to create an application that content will be generated in. This calls CleanSpeak's /system/application end-point.

        :parameter application_id: (Optional) The id of the application being created (see the docs for more information).
        :parameter application_request: The application request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type application_id: uuid
        :type application_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/application').url_segment(application_id).request(application_request).post().go()

    def retrieve_application(self, application_id):
        """Calls CleanSpeak to retrieve an application. This calls CleanSpeak's /system/application end-point.

        :parameter application_id: The id of the application being retrieved (see the docs for more information).
        :type application_id: uuid
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/application').url_segment(application_id).get().go()

    def retrieve_applications(self):
        """Calls CleanSpeak to retrieve all of the applications. This calls CleanSpeak's /system/application end-point.

        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/application').get().go()

    def update_application(self, application_id, application_request):
        """Calls CleanSpeak to update an application that was previously created. This calls CleanSpeak's /system/application end-point.

        :parameter application_id: The id of the application being updated (see the docs for more information).
        :parameter application_request: The application request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type application_id: uuid
        :type application_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/application').url_segment(application_id).request(application_request).put().go()

    def deleted_application(self, application_id):
        """Calls CleanSpeak to delete an application. This calls CleanSpeak's /system/application end-point.

        :parameter application_id: The id of the application being deleted (see the docs for more information).
        :type application_id: uuid
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/application').url_segment(application_id).delete().go()

    def create_moderator(self, moderator_id, moderator_request):
        """Calls CleanSpeak to create an admin/moderator that will have access to the CleanSpeak Management Interface. This calls CleanSpeak's
        /system/user end-point.

        :parameter moderator_id: (Optional) The id of the admin/moderator being created (see the docs for more information).
        :parameter moderator_request: The admin/moderator request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type moderator_id: uuid
        :type moderator_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/user').url_segment(moderator_id).request(moderator_request).post().go()

    def retrieve_moderator(self, moderator_id):
        """Calls CleanSpeak to retrieve an admin/moderator that has access to the CleanSpeak Management Interface. This calls CleanSpeak's
        /system/user end-point.

        :parameter moderator_id: The id of the admin/moderator being retrieved (see the docs for more information).
        :type moderator_id: uuid
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/user').url_segment(moderator_id).get().go()

    def update_moderator(self, moderator_id, moderator_request):
        """Calls CleanSpeak to update an admin/moderator that will have access to the CleanSpeak Management Interface. This calls CleanSpeak's
        /system/user end-point.

        :parameter moderator_id: The id of the admin/moderator being updated (see the docs for more information).
        :parameter moderator_request: The admin/moderator request that is converted to JSON and sent to CleanSpeak (see the docs for more information)
        :type moderator_id: uuid
        :type moderator_request: object
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/user').url_segment(moderator_id).request(moderator_request).put().go()

    def deleted_moderator(self, moderator_id):
        """Calls CleanSpeak to delete an admin/moderator that will have access to the CleanSpeak Management Interface. This calls CleanSpeak's
        /system/user end-point.

        :parameter moderator_id: The id of the admin/moderator being deleted (see the docs for more information).
        :type moderator_id: uuid
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/user').url_segment(moderator_id).delete().go()

    def backup(self):
        """Calls CleanSpeak to download a backup of the database as a ZIP file. This calls CleanSpeak's /system/backup end-point.

        You should call the ClientResponse#write_response_to_file(file) to write out the streamed response to a file.

        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/backup').stream_response().get().go()

    def restore(self, file):
        """Calls CleanSpeak to restore the database from a backup ZIP file. This calls CleanSpeak's /system/restore end-point.

        :parameter file: The backup ZIP file to restore from.
        :type file: file
        :returns: A ClientResponse object that contains the response information from the API call.
        """
        return self.start().uri('/system/restore').post().content_type('application/octet-stream').request_from_file(file).go()

    def start(self):
        return RESTClient().authorization(self.api_key).url(self.base_url)


class RESTClient:
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
        self._request_file = None
        self._stream_response = False
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
        if self._method == 'DELETE':
            return ClientResponse(requests.delete(self._url, headers=self._headers, params=self._parameters))
        elif self._method == 'GET' and self._stream_response:
            return ClientResponse(requests.get(self._url, headers=self._headers, params=self._parameters, stream=True), True)
        elif self._method == 'GET':
            return ClientResponse(requests.get(self._url, headers=self._headers, params=self._parameters, stream=False))
        elif self._method == 'POST' and self._headers['Content-Type'] == 'application/json':
            return ClientResponse(requests.post(self._url, data=None, json=self._request, headers=self._headers, params=self._parameters))
        elif self._method == 'PUT' and self._headers['Content-Type'] == 'application/json':
            return ClientResponse(requests.put(self._url, data=None, json=self._request, headers=self._headers, params=self._parameters))
        elif self._method == 'POST' and self._request_file is not None:
            with open(self._request_file, 'rb') as f:
                return ClientResponse(requests.post(self._url, data=f, headers=self._headers, params=self._parameters))
        elif self._method == 'PUT' and self._request_file is not None:
            with open(self._request_file, 'rb') as f:
                return ClientResponse(requests.put(self._url, data=f, headers=self._headers, params=self._parameters))
        else:
            raise ValueError('The HTTP method must be set to POST, PUT, GET or DELETE prior to calling go()')

    def post(self):
        self._method = 'POST'
        return self

    def put(self):
        self._method = 'PUT'
        return self

    def request(self, request):
        self.content_type('application/json')
        self._request = request
        return self

    def request_from_file(self, file):
        self._request_file = file
        return self

    def stream_response(self):
        self._stream_response = True
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


class ClientResponse:
    """The ClientResponse returned from the the CleanSpeak API.

    Attributes:
        error_response:
        exception:
        response: The full response object
        success_response:
        status:
    """

    def __init__(self, response, streaming=False):
        self.error_response = None
        self.exception = None
        self.response = response
        self.success_response = None
        self.status = response.status_code

        if self.status < 200 or self.status > 299:
            if self.response.content is not None and self.status != 404:
                if self.status == 400:
                    self.error_response = self.response.json()
                else:
                    self.error_response = self.response
        elif not streaming:
            try:
                self.success_response = self.response.json()
            except ValueError:
                self.success_response = None

    def was_successful(self):
        return 200 <= self.status <= 299 and self.exception is None

    def write_response_to_file(self, file):
        with open(file, 'wb') as f:
            for chunk in self.response:
                f.write(chunk)