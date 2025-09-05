"""problem we are using loops but not managable in large data
we need a faster way then this"""
prices = [10,20,30,40,50]

discount = 10 #10% discount sab prize mai karna hai

new_prices = []

for price in prices:
    new_price = price - (price* discount/100)
    new_prices.append(new_price)


print(new_prices)

""" SOLUTION"""
import numpy as np
prices1 = np.array([10,20,30,40,50])

prices1 = prices1 - (prices1 * discount/100)

print(prices1)