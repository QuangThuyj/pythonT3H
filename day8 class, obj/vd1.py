class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city
    def __str__(self):
        return self.street + ',' + self.city

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def introduce(self):
        print(f'Ten toi la {self.name}, song o {self.address}')

    def moveTO(self, new_address):
        self.address = new_address

    def __str__(self):
        return f'{self.name}@{self.address}'

class Student(Person, User):
    def __init__(self, name, address, course, username, password):
        self.name = name
        self.address = address
        self.course = course
        self.username = username
        self.password = password

    def introduce(self):
        super().introduce()
        print(f'Tôi học khóa {self.course}')



addr = Address('123, Ba Dinh', ' Ha Noi')
st = Student('Nguyen Van A', addr, 'Python 1911E', 'test', 'abc123')
st.introduce()
#p = Person('Nguyen Van A', addr)
#p.moveTO('TP. HCM')
# p.introduce() #Person.introduce(p)
# print(p)