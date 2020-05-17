#product = (code, name, price)
product = ('001', 'sua hop', 10000)
code, name, price = product
print(code, name, price)

sale_item = ('001', 10000, 5)
code, price, qty = sale_item

sale_item = [
    ('001', 10000, 5),
    ('002', 20000, 2),
    ('001', 12000, 10)
]

s = 0

for item in sale_item:
    code, price, qty = item
    s += price*qty

print(s)
