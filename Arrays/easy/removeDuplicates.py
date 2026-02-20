class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return 0
        
        i = 0
        
        for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
        
        return i + 1


# How It Works (Explain in Interview)
# i → slow pointer (tracks unique elements)
# j → fast pointer (scans array)
# When a new unique element is found → move it to next position
# Return i + 1 as the count of unique elements

# ✅ Test Case 1 (Normal Case)
# arr = [1,1,2]
# After function call:
# sol = Solution()
# k = sol.removeDuplicates(arr)
# print(k)        # 2
# print(arr[:k])  # [1,2]

# ✅ Test Case 2 (Multiple Duplicates)
# arr = [0,0,1,1,1,2,2,3,3,4]
# Output:
# k = 5
# arr[:k] = [0,1,2,3,4]

# ✅ Test Case 3 (No Duplicates)
# arr = [1,2,3]
# Output:
# k = 3
# arr[:k] = [1,2,3]

# ✅ Test Case 4 (All Same)
# arr = [2,2,2,2]
# Output:
# k = 1
# arr[:k] = [2]