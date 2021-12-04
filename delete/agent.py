import json
import time
from json.decoder import JSONDecodeError
import requests
# 2 browser, 3 platform, 5 device
exclude_params = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"
# response1 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check")

response2 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                         headers={"User-Agent": exclude_params}
                         )
print(response2.content)
obj = json.loads(response2.content)
print(obj['platform'])
print(obj['browser'])
print(obj['device'])