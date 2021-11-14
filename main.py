from json.decoder import JSONDecodeError
import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
count_of_redirects = len(response.history) - 1
print(f"count_of_redirects = {count_of_redirects}")
print(f"end url = {response.history[count_of_redirects].url}")
