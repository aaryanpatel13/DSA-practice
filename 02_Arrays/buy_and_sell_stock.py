# You are given an array prices where prices[i] is the price of a given stock on the 'i'th day.
# Return the max profit one can make by buying and selling the stock.
# Input: prices = [7,1,5,3,6,4]
# Output: 5 ; Buy stock in price[1](day 2) and sell it on price[4](day 5) to maimize the profit
# NOTE: buy at price[1] and sell it on price[0] is not possible as we have to buy first then only we can sell it.

def maxProfit(prices):
    n = len(prices)
    mini = prices[0] # buy stock on this day as let this is the minimum price of stock 
    max_profit = 0

    for i in range(n):
        profit = prices[i] - mini
        max_profit = max(max_profit,profit)
        mini = min(mini, prices[i])
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
