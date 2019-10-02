
import requests

api_url = "http://shibe.online/api/shibes?count=1"
response = requests.get(api_url, {"count": 10})

print(f"Response status code is: {response.status_code}")
image_url = response.json()
print(image_url)
