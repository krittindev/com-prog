def total(pocket):
    total_money = 0
    for cash, amount in pocket.items():
        total_money += cash * amount
    return total_money


def take(pocket, money_in):
    for cash, amount in money_in.items():
        if cash in pocket:
            pocket[cash] += amount
        else:
            pocket[cash] = amount


def pay(pocket, amt):
    copy_amt = amt
    pay_pocket = {}
    if total(pocket) < amt:
        return {}
    cashes = []
    for cash, _ in pocket.items():
        cashes.append(cash)
    for cash in sorted(cashes, reverse=True):
        if cash < copy_amt:
            to_cash_amount = min(copy_amt // cash, pocket[cash])
            pay_pocket[cash] = to_cash_amount
            copy_amt -= to_cash_amount * cash
            pocket[cash] -= to_cash_amount
    if copy_amt != 0:
        for key, value in pay_pocket.items():
            pocket[key] += value
        return {}
    return pay_pocket


exec(input().strip())
