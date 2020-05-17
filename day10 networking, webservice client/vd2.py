import requests, json
url = "https://translation.googleapis.com/language/translate/v2?key=AIzaSyBSut2ax6ct7NAMGELpAZ_bRxNVuDS-ZRU"
data = {
    'q': "Hôm nay là thứ ba",
    'source': 'vi',
    'target': 'en',
    'format': 'text'
}

body = json.dumps(data)
req = requests.post(url, data=body)
obj = json.loads(req.text)
print(obj['data']['translations'][0]['translatedText'])
