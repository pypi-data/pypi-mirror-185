# strapi-api-client

Strapi API Client is used for maintaining a communication with the [Strapi CMS](https://strapi.io/) by HTTP transfer protocol.

> **IMPORTANT NOTE**: For now, dependency is in a testing phase and is used for a very specific use cases. It still needs
> more modular and configurable way to be used by a community.

## Installation

```python
# pip
pip install strapi-api-client

# pipenv
pipenv install strapi-api-client

# poetry
poetry add strapi-api-client
```

## Example

#### 1. Create ApiClient object

```python
import os

from strapi_api_client.api_client import ApiClient

api_client = ApiClient(
    api_url=os.getenv('API_URL'),
    api_key=os.getenv('API_KEY'),
    timeout=60
)
```

#### 2. Create request to Strapi with an Api Client

> This request will return a dictionary as a result.

```python
community_response = api_client.community.get_community(name='my-community')
```

## Tests

To run tests, you need to run command: `pytest`

Tests require access data to the api. For security reasons, access data is stored in environment variables. To set
environment variables, you need to create an `.env` file from the example in the `.env.example` file.

---
Developed with 💙 and ☕️ by [Adam Žúrek](https://zurek11.github.io/)
with the support of [CulturePulse.ai](https://www.culturepulse.ai/), 2023 (C)
