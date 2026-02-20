class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        # Step 1: Find first decreasing element from right
        index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        
        # If no such index, reverse entire array
        if index == -1:
            nums.reverse()
            return
        
        # Step 2: Find element just greater than nums[index]
        for j in range(n - 1, index, -1):
            if nums[j] > nums[index]:
                nums[j], nums[index] = nums[index], nums[j]
                break
        
        # Step 3: Reverse the right half
        nums[index + 1:] = reversed(nums[index + 1:])

#how it works
# 💡 Idea:
# Traverse from right → find first decreasing element
# Find next greater element on right
# Swap them
# Reverse the remaining right portion
# This gives next lexicographically greater permutation.


# ✅ Test Case 1
# nums = [1,2,3]
# Output:
# [1,3,2]

# ✅ Test Case 2
# nums = [3,2,1]
# Output:
# [1,2,3]

# ✅ Test Case 3
# nums = [1,1,5]
# Output:
# [1,5,1]