import requests, json, base64
url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBSut2ax6ct7NAMGELpAZ_bRxNVuDS-ZRU"
with open('sample.jpg', 'rb') as f:
    b64data = base64.b64encode(f.read())

data = {
    "requests": [
        {
            "image": {"content": b64data.decode()},
            "features": [{"type": "DOCUMENT_TEXT_DETECTION"}]
        },
    ]
}

req = requests.post(url, data=json.dumps(data))
with open('result.json', 'w', encoding='utf-8') as f:
    f.write(req.text)
obj = json.loads(req.text)
print(obj['responses'][0]['fullTextAnnotation']['text'])