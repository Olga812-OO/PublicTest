import os
print(os.listdir())

import json

with open('orders_july_2023.json', 'r') as my_file:
    orders_july_2023 = json.load(my_file)
    print(orders_july_2023)

# 1.Какой номер самого дорогого заказа за июль?
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders_july_2023.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1.Номер самого дорогого заказа в июле: {max_order}, стоимость заказа: {max_price}')

# 2.Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_order_num = None
for order_num, orders_data in orders_july_2023.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order_num = order_num
        max_quantity = quantity
print(f'2.Номер заказа с самым большим количеством товаров: {max_order_num}')

# 3.В какой день в июле было сделано больше всего заказов?
date_dict = {}
for order_num, orders_data in orders_july_2023.items():
    date = orders_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1

for date in sorted(date_dict):
    max_value = max(date_dict.values())
    if date_dict[date] == max_value:
     print(f'3.Больше всего заказов было сделано в {date}: {date_dict[date]}')

# 4.Какой пользователь сделал самое большое количество заказов за июль?
max_orders = 0
user_dict = {}

for order_num, orders_data in orders_july_2023.items():
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + 1
    orders = user_dict.get(user_id)
    if orders > max_orders:
        max_orders = orders
        print(f'4.Самое большое количество заказов за июль: {max_orders} сделал пользователь под номером: {user_id}')

# 5.У какого пользователя самая большая суммарная стоимость заказов за июль?
max_sum = 0
max_price_user = None
for order_num, orders_data in orders_july_2023.items():
    user_id = orders_data['user_id']
    price = orders_data['price']
    sum_of_prices = sum(price for _ in range(price))
    if max_sum < sum_of_prices:
        max_sum = sum_of_prices
        max_price_user = user_id
print(f'5.Самая большая суммарная стоимость заказов за июль: {max_sum} у пользователя под номером: {max_price_user}')

# 6.Какая средняя стоимость заказа была в июле?
from statistics import mean
prices = []

for order_num, orders_data in orders_july_2023.items():
    prices.append(orders_data['price'])
avg_price = mean(prices)
print(f'6.Средняя стоимость заказа была в июле: {round(avg_price, 2)}')

# 7.Какая средняя стоимость товаров в июле?
sum_of_prices = 0
sum_of_quantity = 0
for order_num, orders_data in orders_july_2023.items():
    sum_of_prices += orders_data['price']
    sum_of_quantity += orders_data['quantity']
avg_price_quantity = sum_of_prices / len(orders_july_2023) + sum_of_quantity / len(orders_july_2023)
print(f'7.Средняя стоимость товаров в июле: {avg_price_quantity}')