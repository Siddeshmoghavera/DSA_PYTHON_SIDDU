class Solution:
    def moveZeroes(self, arr):
        nonZ = 0  # position to place next non-zero
        
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[nonZ] = arr[nonZ], arr[i]
                nonZ += 1
                
# ✔ Moves all zeroes to end
# ✔ Maintains relative order
# ✔ In-place (no extra array)

# Time & Space Complexity (Say This in Interview)
# Time Complexity: O(n)
# Space Complexity: O(1)

# ✅ Test Case 1 (Normal Case)
# arr = [0,1,0,3,12]
# Output:
# [1,3,12,0,0]

# ✅ Test Case 2 (No Zero)
# arr = [1,2,3]
# Output:
# [1,2,3]

# ✅ Test Case 3 (All Zeroes)
# arr = [0,0,0]
# Output:
# [0,0,0]

# ✅ Test Case 4 (Zero at End)
# arr = [1,2,0]
# Output:
# [1,2,0]