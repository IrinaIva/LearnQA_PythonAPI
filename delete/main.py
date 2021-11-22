from json.decoder import JSONDecodeError
import requests
# 1
response1 = requests.post("https://playground.learnqa.ru/api/compare_query_type")
print(response1.text)
print(response1.status_code)
print(response1.url)
# Wrong method provided
# 200
# https://playground.learnqa.ru/api/compare_query_type

# 2
response2 = requests.head("https://playground.learnqa.ru/api/compare_query_type")
print(response2.text)
print(response2.status_code)
print(response2.url)
#
# 400 # Не удалось обработать запрос, так как он представлен в неправильном формате или является некорректным.
# https://playground.learnqa.ru/api/compare_query_type

# 3
payload = {"method": "GET"}
response3 = requests.get("https://playground.learnqa.ru/api/compare_query_type", params=payload)
print(response3.text)
print(response3.status_code)
print(response3.url)
# {"success":"!"}
# 200
# https://playground.learnqa.ru/api/compare_query_type?method=GET

# 4
methods = ["GET", "POST", "DELETE", "PUT"]
payload = [{"method": "GET"}, {"method": "POST"}, {"method": "DELETE"}, {"method": "PUT"}]

for method in methods:
    for val in payload:
        if method == "GET":
            response4 = requests.request(method=method, url="https://playground.learnqa.ru/api/compare_query_type",
                                         params=val)
        else:
            response4 = requests.request(method=method, url="https://playground.learnqa.ru/api/compare_query_type",
                                         data=val)

        if val['method'] == method:
            if response4.text != '{"success":"!"}':
                print(response4.text)
                print(f"parameter - {val['method']}")
                print(f"method - {method}")
        elif val["method"] != method:
            if response4.text != "Wrong method provided":
                print(response4.text)
                print(f"parameter - {val['method']}")
                print(f"method - {method}")
# {"success":"!"}
# parameter - GET
# method - DELETE

