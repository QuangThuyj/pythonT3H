import json, base64
def fileToBase64(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        b64data = base64.b64encode(data)
        return b64data.decode() #convert to str

class Student:
    def __init__(self, name, address, img_file):
        self.name = name
        self.address = address
        self.img_file = img_file

    def toJson(self):
        return json.dumps({
            'name': self.name,
            'address': self.address,
            'image': fileToBase64('image.jpg')
        })

st = Student('Nguyen Van A', 'Ha Noi', 'image.jpg')
with open('student.json', 'w') as f: f.write(st.toJson())