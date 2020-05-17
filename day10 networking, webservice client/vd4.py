import requests, json
url = "http://api.openweathermap.org/data/2.5/forecast?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9&cnt=8"
req = requests.get(url)
obj = json.loads(req.text)
for item in obj['list']:
    dt = item['dt_txt']
    temp = item['main']['temp']
    print(dt, ":", temp)