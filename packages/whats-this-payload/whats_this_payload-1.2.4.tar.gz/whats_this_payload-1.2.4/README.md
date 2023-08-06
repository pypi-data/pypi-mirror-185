# whats-this-payload

[![Build Status](https://github.com/Tomperez98/whats-this-payload/workflows/test/badge.svg?branch=main&event=push)](https://github.com/Tomperez98/whats-this-payload/actions?query=workflow%3Atest)
![black-python-styleguide](https://img.shields.io/badge/code%20style-black-000000.svg)

-----

## Inspiration
Working with payload from webhooks can be really anoying. This tries to make the process easier.

## How to run?
- Create a virtual environment
- Activate the environment
- run `make install env=dev`

## Install
```bash
pip install whats-this-payload
```

## Basic usage
```python
from whats_this_payload import get_identifier

whatsapp_identifier = get_identifier(webhook="whatsapp") # or any other available integration.

webhook_payload_as_dict = payload.dict()

payload_type = whatsapp_identifier(
    payload=webhook_payload_as_dict
).identify_payload_type()

print(payload_type)
# >> PayloadType.ANSWER_FROM_LIST_MESSAGE

# Supported payloads 
# (https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/payload-examples#list-messages)
```