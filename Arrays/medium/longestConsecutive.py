class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Start only if it's the beginning of a sequence
            if (num - 1) not in num_set:
                current = num
                count = 1
                
                while (current + 1) in num_set:
                    current += 1
                    count += 1
                
                longest = max(longest, count)
        
        return longest


# 💡 Key Idea:
# Use a HashSet for O(1) lookups.
# Only start counting when num - 1 is NOT present.
# That ensures we start only at beginning of sequences.
# Expand forward to count length.
# This avoids sorting → gives O(n) time.



# ✅ Test Case 1 (Classic Case)
# nums = [100,4,200,1,3,2]
# Output:
# 4
# Sequence → [1,2,3,4]

# ✅ Test Case 2 (With Duplicates)
# nums = [0,3,7,2,5,8,4,6,0,1]
# Output:
# 9
# Sequence → [0,1,2,3,4,5,6,7,8]

# ✅ Test Case 3 (Single Element)
# nums = [10]
# Output:
# 1

# ✅ Test Case 4 (Empty Array)
# nums = []
# Output:
# 0