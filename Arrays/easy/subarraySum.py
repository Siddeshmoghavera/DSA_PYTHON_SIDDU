class Solution:
    def subarraySum(self, nums, k):
        total_sum = 0
        result = 0
        preSum = {0: 1}   # base case
        
        for num in nums:
            total_sum += num
            
            if (total_sum - k) in preSum:
                result += preSum[total_sum - k]
            
            preSum[total_sum] = preSum.get(total_sum, 0) + 1
        
        return result

# How It Works:
# total_sum → cumulative sum of elements
# preSum → dictionary to count occurrences of cumulative sums
# For each element:
# 1. Update total_sum
# 2. Check if (total_sum - k) exists in preSum → if yes
#    it means there is a subarray that sums to k
# 3. Update preSum with the current total_sum count

# ✅ Test Case 1 (Basic Case)
# nums = [1,1,1]
# k = 2
# Output:
# 2
# Subarrays → [1,1] (twice)

# ✅ Test Case 2 (With Negative Numbers)
# nums = [1,2,3]
# k = 3
# Output:
# 2
# Subarrays → [1,2], [3]

# ✅ Test Case 3 (Contains Negative Values)
# nums = [1,-1,0]
# k = 0
# Output:
# 3
# Subarrays → [1,-1], [0], [1,-1,0]