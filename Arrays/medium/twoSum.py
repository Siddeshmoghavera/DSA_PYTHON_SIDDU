class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[nums[i]] = i


# How it works
# Idea:
# For each number, compute target - current_number
# Check if that value already exists in hashmap
# If yes → return indices
# Otherwise → store current number with its index 


# ✅ Test Case 1
# nums = [2,7,11,15]
# target = 9
# Output:
# [0,1]

# ✅ Test Case 2
# nums = [3,2,4]
# target = 6
# Output:
# [1,2]

# ✅ Test Case 3
# nums = [3,3]
# target = 6
# Output:
# [0,1]