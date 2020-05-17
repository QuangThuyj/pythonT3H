import base64

with open('image.jpg', 'rb') as f:
    data = f.read()
    # print(data.__class__, len(data))
    b64data = base64.b64encode(data)
    print(len(b64data))

with open('imgbase64.txt', 'wb') as f:
    f.write(b64data)