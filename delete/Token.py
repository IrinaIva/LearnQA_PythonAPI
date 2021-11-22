import json
import time
from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=response.json())
if response2.json()["status"] != "Job is NOT ready":
    print(f"Status is incorrect for response2 - {response2.json()['status']}")
time.sleep(response.json()['seconds'])
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=response.json())
if response3.json()["status"] != "Job is ready":
    print(f"Status is incorrect for response3 - {response3.json()['status']}")
try:
    result = response3.json()["result"]
except:
    print(f"Result field is missing")
