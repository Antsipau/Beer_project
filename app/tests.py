
import unittest
from unittest.mock import Mock
import json

import requests
def client():
    return requests.get(
        'http://127.0.0.1:8000/api_test1',
        {
            'id': 1,
            'manufacturer': 'Selfmade Brewery',
            'price': 9.50
        }
    ).text
# Create your tests here.

print(client())