class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        ans = [0] * n
        pos = 0
        neg = 1
        
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
        
        return ans

#How It Works:
# 💡 Idea:
# Create new array
# Place positive numbers at even indices (0,2,4...)
# Place negative numbers at odd indices (1,3,5...)
# Problem guarantees equal number of positives and negatives


# ✅ Test Case 1
# nums = [3,1,-2,-5,2,-4]
# Output:
# [3,-2,1,-5,2,-4]

# ✅ Test Case 2
# nums = [-1,1]
# Output:
# [1,-1]

# ✅ Test Case 3
# nums = [1,-1,2,-2]
# Output:
# [1,-1,2,-2]