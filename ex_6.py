i = 1
goods = []
n = int(input("How many goods do you want? "))
for _ in range(n):
    name = input("The name ")
    price = input("Price ")
    quant = input("Quantity ")
    measure = input("Measure ")
    goods.append((i, {'name': name, 'price': price, 'quantity': quant, 'measure': measure}))
    i += 1
print(goods)
goods_dict = {'name': [], 'price': [], 'quantity': [], 'measure': []}
for good in goods:
    goods_dict['name'].append(good[1]['name'])
    goods_dict['price'].append(good[1]['price'])
    goods_dict['quantity'].append(good[1]['quantity'])
    if good[1]['measure'] not in goods_dict['measure']:
        goods_dict['measure'].append(good[1]['measure'])
print(goods_dict)
