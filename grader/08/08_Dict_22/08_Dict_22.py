ice_cream_price = {}
sales_amount = {}
sales_ice_cream_price = {}

n_ice_cream = int(input())
for _ in range(n_ice_cream):
    name, price = input().strip().split()
    price = float(price)
    ice_cream_price[name] = price
    sales_ice_cream_price[name] = 0


n_sales = int(input())
for _ in range(n_sales):
    name, amount = input().strip().split()
    amount = int(amount)
    if name in ice_cream_price:
        price = ice_cream_price[name]
        sales_ice_cream_price[name] += amount * price

total = sum([price for price in sales_ice_cream_price.values()])
top_sales_price = max([price for price in sales_ice_cream_price.values()])
top_sales_name = sorted(
    [name for name, price in sales_ice_cream_price.items() if price == top_sales_price])
if total == 0:
    print('No ice cream sales')
else:
    print('Total ice cream sales: %.1f\nTop sales: %s' % (
        total,
        ', '.join(top_sales_name)
    ))
