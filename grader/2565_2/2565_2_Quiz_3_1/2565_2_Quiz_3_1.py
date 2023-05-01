# 33

company_rates = {}
stock_prices = {}
rate_prices = {}
total_price = 0

while True:
    line = input().strip()

    if line == "END":
        break

    company, _rate = line.split()
    rate = _rate[:len(_rate) - (1 if _rate[-1] in "+-" else 0)]
    if _rate[-1] in "+-":
        rate
    company_rates[company] = rate

while True:
    line = input().strip()

    if line == "END":
        break

    stock, _price = line.split()
    price = int(_price)
    stock_prices[stock] = price

for stock, price in stock_prices.items():
    total_price += price
    index_first_number = 0
    for i in range(len(stock) - 1, -1, -1):
        if stock[i] in '1234567890':
            index_first_number = i
    prefix = stock[:index_first_number]
    rate = "None"
    if prefix in company_rates:
        rate = company_rates[prefix]

    if rate not in rate_prices:
        rate_prices[rate] = price
    else:
        rate_prices[rate] += price

for rating_group in ['AAA', 'AA', 'A', 'BBB', 'BB', 'B', 'CCC', 'CC', 'C', 'D', 'None']:
    if rating_group in rate_prices:
        price = rate_prices[rating_group]
        percentage = round(price / total_price * 100, 2)
        print("%s %d %.2f%%" % (rating_group, price, percentage))
