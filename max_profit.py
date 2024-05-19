def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit



prices1 = [7, 1, 5, 3, 6, 4]
print(max_profit(prices1))

prices2 = [7, 6, 4, 3, 1]
print(max_profit(prices2))
