import requests, json
url = "http://api.openweathermap.org/data/2.5/weather?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9"
req = requests.get(url)
obj = json.loads(req.text)
print('Nhiet do hien tai', obj['main']['temp'])
