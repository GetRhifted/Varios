from urllib.request import urlopen
import json

url = "https://gsi.fly.dev/characters/6"
response = urlopen(url)
data = json.loads(response.read())
print(data)
