class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        profit = 0
        buy_day = -1
        sell_day = -1
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                buy_day = i
            
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
                sell_day = i
        
        print(buy_day, sell_day)
        return profit


# How to Explain
# At each day:
# Track the minimum price so far
# Calculate potential profit if sold today
# Update maximum profit
# This is similar to Kadane’s idea but for difference tracking


# ✅ Test Case 1 (Normal Case)
# prices = [7,1,5,3,6,4]
# Output:
# 5
# Buy at 1 (index 1)
# Sell at 6 (index 4)

# ✅ Test Case 2 (No Profit)
# prices = [7,6,4,3,1]
# Output:
# 0
# No transaction

# ✅ Test Case 3 (Single Element)
# prices = [5]
# Output:
# 0