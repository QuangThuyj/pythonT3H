import base64
with open('imgbase64.txt') as f:
    b64data = f.read()
    data = base64.b64decode(b64data)

with open('output.jpg', 'wb') as f:
    f.write(data)

