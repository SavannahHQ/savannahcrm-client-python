# Savannah CRM Client

This client library wraps the [Savannah CRM API](https://docs.savannahhq.com/api/), making it easier to import community members and activity from your own Python code.

## Install

```
pip install savannahcrm-client
```

# Usage

## Connecting to an API Source

```
>>> from savannahcrm import SavannahAPISource

>>> source = SavannahAPISource(token='7fbd4b88-5af7-4acf-bc81-f1888cd8f1b2')

>>> print("Source: %s" % source)
Source: Test

>>> print("Source info: %s" % source.info)
Source info: {'community': 'InfluxDB', 'name': 'Test', 'icon_name': 'fab fa-twitter-square', 'first_import': None, 'last_import': '2021-04-20T14:20:12.440415', 'enabled': True}
```

## Adding a Member

```
>>> new_member = source.add_member(
...     origin_id='test-1',
...     username='test_user_1',
...     name='API Test User',
...     email='api@test.com',
...     tags=['api-test']
... )

>>> print("Member: %s" % new_member)
Member: {'origin_id': 'test-1', 'username': 'test_user_1', 'name': 'API Test User', 'email': 'api@test.com', 'avatar': None, 'tags': ['api-test']}
```

## Adding a Converation

```
>>> convo_tstamp = datetime.datetime(2021, 4, 19, 13, 35, 00)

>>> new_convo = source.add_conversation(
...     origin_id='test-convo-1',
...     speaker='test-1',
...     channel='API Test',
...     timestamp=convo_tstamp,
...     content='Testing savannah-client library for Python',
...     location='https://docs.savannahhq.com/api/',
...     tags=['api-test', 'python']
... )

>>> print("Conversation: %s" % new_convo)
Conversation: {'origin_id': 'test-convo-1', 'speaker': 'test-1', 'channel': 'API Test', 'timestamp': '2021-04-19T13:35:00', 'content': 'Testing savannah-client library for Python', 'location': 'https://docs.savannahhq.com/api/', 'participants': ['test-1'], 'tags': ['api-test', 'python']}
```

## Adding a Contribution

```
>>> new_contrib = source.add_contribution(
...     origin_id='test-convo-1',
...     author='test-1',
...     channel='API Test',
...     contribution_type='Pull Request',
...     timestamp=convo_tstamp,
...     title='Built importer using the Savannah API',
...     location='https://github.com/SavannahHQ/savannahcrm-client-python',
...     tags=['api-test', 'python'],
...     conversation='test-convo-1',
... )

>>> print("Contribution: %s" % new_contrib)
Contribution: {'origin_id': 'test-convo-1', 'author': 'test-1', 'contribution_type': 'Pull Request', 'channel': 'API Test', 'timestamp': '2021-04-19T13:35:00', 'title': 'Built importer using the Savannah API', 'location': 'https://github.com/SavannahHQ/savannahcrm-client-python', 'conversation': 'test-convo-1', 'tags': ['api-test', 'python']}
```