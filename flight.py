import requests
import json

url = "http://localhost:1337/api/flights/3?populate=*"

payload = ""
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
