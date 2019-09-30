
import requests

api_url = "http://shibe.online/api/shibes?count=1"
response = requests.get(api_url)

print(f"Response status code is: {response.status_code}")
print(response.json())
