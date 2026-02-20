# Kadane’s Algorithm (Maximum Subarray Sum)

class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    
# ✅ Test Case 1 (Classic Example)
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output:
# 6
# Subarray → [4,-1,2,1]

# ✅ Test Case 2 (All Positive)
# nums = [1,2,3,4]
# Output:
# 10

# ✅ Test Case 3 (All Negative)
# nums = [-3,-2,-1]
# Output:
# -1

# ✅ Test Case 4 (Single Element)
# nums = [5]
# Output:
# 5