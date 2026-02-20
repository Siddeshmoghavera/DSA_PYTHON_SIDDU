class Solution:
    def check(self, nums):
        count = 0
        n = len(nums)
        
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                count += 1
        
        if nums[n - 1] > nums[0]:
            count += 1
        
        return count <= 1
    


# Count how many times the order decreases (nums[i-1] > nums[i]).
# If the array is sorted and rotated, there should be at most one such decrease.
# Also check the last and first element comparison.
# If count <= 1, return True, otherwise False.


# ✅ Test Case 1
# nums = [3, 4, 5, 1, 2]
# Output: True
# 👉 It is sorted [1,2,3,4,5] and rotated once.

# ✅ Test Case 2
# nums = [1, 2, 3, 4, 5]
# Output: True
# 👉 Already sorted (rotation 0 times).

# ❌ Test Case 3
# nums = [2, 1, 3, 4]
# Output: False
# 👉 Not sorted + rotated properly.