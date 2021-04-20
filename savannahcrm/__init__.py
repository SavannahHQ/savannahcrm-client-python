import requests
import json
import datetime

def default_json_encoder(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

class SavannahAPISource(object):
    TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
    SOURCE_ENDPOINT = '/api/v1/'
    IDENTITY_ENDPOINT = '/api/v1/identity/'
    CONVERSATION_ENDPOINT = '/api/v1/conversation/'
    CONTRIBUTION_ENDPOINT = '/api/v1/contribution/'
    
    def __init__(self, token, host='https://savannahcrm.com'):
        self.host = host
        self.token = token
        self._api_headers = {
            'Authorization': 'token %s' % self.token,
            'Content-Type': 'application/json',
        }
        self._metadata = None

    def _api_call(self, endpoint, payload=None):
        if payload is None:
            resp = requests.get(self.host + endpoint, headers=self._api_headers)
        else:
            data = json.dumps(payload, default=default_json_encoder)
            resp = requests.post(self.host + endpoint, data=data, headers=self._api_headers)
        if resp.status_code == 200 or resp.status_code == 201:
            data = resp.json()
            return data
        else:
            raise RuntimeError("API call failed (%s): %s" % (resp.status_code, resp.content))

    @property
    def info(self):
        if self._metadata is None:
            self._metadata = self._api_call(self.SOURCE_ENDPOINT)
        return self._metadata

    def add_member(self, origin_id, username=None, name=None, email=None, avatar=None, tags=None):
        if username is None:
            username = origin_id

        member_data = {
            'origin_id': origin_id,
            'username': username,
        }
        if name:
            member_data['name'] = name
        if email:
            member_data['email'] = email
        if avatar:
            member_data['avatar'] = avatar
        if tags:
            member_data['tags'] = tags
        return self._api_call(self.IDENTITY_ENDPOINT, member_data)
        
    def add_conversation(self, origin_id, speaker, channel, timestamp, content=None, location=None, participants=None, tags=None):
        convo_data = {
            'origin_id': origin_id,
            'speaker': speaker,
            'channel': channel,
            'timestamp': timestamp,
            'content': content
        }
        if location:
            convo_data['location'] = location
        if participants:
            convo_data['participants'] = participants
        if tags:
            convo_data['tags'] = tags
        return self._api_call(self.CONVERSATION_ENDPOINT, convo_data)

    def add_contribution(self, origin_id, author, channel, timestamp, title, contribution_type, location=None, tags=None, conversation=None):
        contrib_data = {
            'origin_id': origin_id,
            'author': author,
            'channel': channel,
            'timestamp': timestamp,
            'title': title,
            'contribution_type': contribution_type,
        }
        if location:
            contrib_data['location'] = location
        if conversation:
            contrib_data['conversation'] = conversation
        if tags:
            contrib_data['tags'] = tags
        return self._api_call(self.CONTRIBUTION_ENDPOINT, contrib_data)

    def __str__(self):
        return self.info['name']
