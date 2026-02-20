class Solution:
    def sortColors(self, nums):
        if not nums:
            return
        
        c0 = c1 = c2 = 0
        
        # Count occurrences
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        
        # Overwrite array
        i = 0
        
        while c0 > 0:
            nums[i] = 0
            i += 1
            c0 -= 1
        
        while c1 > 0:
            nums[i] = 1
            i += 1
            c1 -= 1
        
        while c2 > 0:
            nums[i] = 2
            i += 1
            c2 -= 1

# How It Works:
# Idea:
# Count number of 0s, 1s, and 2s
# Rewrite the array using those counts


# ✅ Test Case 1
# nums = [2,0,2,1,1,0]
# Output:
# [0,0,1,1,2,2]

# ✅ Test Case 2
# nums = [2,0,1]
# Output:
# [0,1,2]

# ✅ Test Case 3
# nums = [0]
# Output:
# [0]