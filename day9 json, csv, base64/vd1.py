import json

student = {
    "name": "Nguyen Van A",
    "age": 20,
    "address": {
        "street": "123 Dong Da",
        "city": "Ha Noi"
    }
}
studentList = [
    {"name": "Nguyen Van A", "address": {"city": "Hanoi", "street": "123"}},
    {"name": "Nguyen Van B", "address": {"street": "456", "city": "TPHCM"}}
]
print(json.dumps(student))
print(json.dumps(studentList))

# print(student.__class__)
# print(jsonSt.__class__)