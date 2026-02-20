class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        
        return max_count
    
# How It Works:
# count → tracks current consecutive 1s
# max_count → stores maximum consecutive 1s found
# Reset count when a 0 appears
# Update maximum whenever needed


# ✅ Test Case 1
# nums = [1, 1, 0, 1, 1, 1]
# 🔎 Explanation:
# First two 1s → count = 2
# Then 0 → reset
# Last three 1s → count = 3
# ✅ Output:
# 3

# ✅ Test Case 2
# nums = [1, 0, 1, 1, 0, 1]
# ✅ Output:
# 2

# ✅ Test Case 3 (All Ones)
# nums = [1, 1, 1, 1]
# ✅ Output:
# 4