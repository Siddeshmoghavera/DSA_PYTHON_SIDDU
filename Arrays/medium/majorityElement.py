class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
    
# How It Works:
# Key Idea (Boyer–Moore Voting Algorithm)
# If count becomes 0 → choose new candidate
# Same number → increase count
# Different number → decrease count
# Majority element survives cancellation
# Because majority element appears more than n/2 times, it can never be fully canceled.


# ✅ Test Case 1
# nums = [3,2,3]
# Output:
# 3

# ✅ Test Case 2
# nums = [2,2,1,1,1,2,2]
# Output:
# 2

# ✅ Test Case 3 (Single Element)
# nums = [5]
# Output:
# 5