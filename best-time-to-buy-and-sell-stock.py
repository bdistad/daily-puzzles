'''
Source: LeetCode

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''


from typing import List
def max_profit(prices: List[int]) -> int:
    
    max_profit = int()
    for i in range(0,len(prices)):
        for x in range(i, len(prices)):
            if prices[x] - prices[i] > max_profit:
                max_profit = prices[x] - prices[i]
    if max_profit > 0:
        return max_profit
    else:
        return 0

test = ["test", "one"]