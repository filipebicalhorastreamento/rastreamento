import requests

url = "https://integration.systemsatx.com.br/Login?Username=filipebicalho.rastreamento%40gmail.com&Password=A%40sU8e1Gzl&Hashcentral=ACB2CC74-D4E2-4835-9E49-41109C43D6CB"

payload = {}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
