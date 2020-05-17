with open('sales.csv', encoding='utf-8') as f:
    header = f.readline().strip()
    lines = f.readlines()

with open('output_sale.csv', 'w', encoding='utf-8') as f:
    new_header = header + ', Sale,Profit'
    f.write(new_header + '\n')
    sale_total, profit_total = 0, 0

    for line in lines:
        stt, product, price, cost, qty = line.strip().split(',')
        sale = int(qty)*float(price)
        profit = int(qty)*(float(price) - float(cost))
        f.write(f'{stt}, {product}, {price}, {cost}, {qty}, {sale}, {profit} \n')
        sale_total += sale
        profit_total += profit
    f.write(f'Total,,,,,{sale_total},{profit_total}')