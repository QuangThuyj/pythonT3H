import json
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def toJson(self):
        return json.dumps({'name': self.name, 'address':{
                    'street': self.address.street,
                    'city': self.address.city
                }
            })

    def importFromFile(filename):
        with open('student1.json') as f:
            obj = json.loads(f.read())
            name = obj['name']
            street = obj['address']['street']
            city = obj['address']['city']
            addr = Address(street, city)
            return Student(name, addr)


addr = Address('123 Dong Da', 'Hanoi')
st = Student('Nguyen Van A', addr)
# print(st.toJson())
with open('student1.json', 'w') as f: f.write(st.toJson())
st2 = Student.importFromFile('student1.json')
print(st2.name, st2.address.street, st2.address.city)