import base64
with open('cfs.txt') as f:
    b64data = f.read()
    data = base64.b64decode(b64data)

with open('output-cfs', 'wb') as f:
    f.write(data)