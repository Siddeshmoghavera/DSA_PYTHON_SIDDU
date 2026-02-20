class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
    
    
# ✅ Test Case 1 (Normal Case)
# nums = [3, 0, 1]
# Output: 2

# ✅ Test Case 2 (Missing Last Number)
# nums = [0, 1]
# Output: 2

# ✅ Test Case 3 (Missing First Number)
# nums = [1, 2, 3]
# Output: 0

# ✅ Test Case 4 (Large Random Order)
# nums = [9,6,4,2,3,5,7,0,1]
# Output: 8