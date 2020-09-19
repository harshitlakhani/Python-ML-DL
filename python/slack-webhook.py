import requests
import json
import sys

data = {
    "text":"hi, this is a test"
}
webhook = sys.argv[1]

requests.post(webhook, json.dumps(data))