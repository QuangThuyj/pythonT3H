sales = [
    {'product':'p1', 'qty':2, 'price': 10000},
    {'product':'p2', 'qty':3, 'price': 15000},
    {'product':'p1', 'qty':3, 'price': 12000},
    {'product':'p3', 'qty':5, 'price': 20000}
]

total_sale = 0
for item in sales:
    total_sale += item['qty']*item['price']

print(total_sale)

count = {}
for item in sales:
    product, qty = item['product'], item['qty']
    count[product] = count.get(product, 0) + qty
# count = sorted(count.items(), key=lambda x: x[1], reversed=True)
print(count)