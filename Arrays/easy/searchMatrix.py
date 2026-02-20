class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        index = -1
        
        # Step 1: Find the correct row
        for i in range(m):
            if matrix[i][n - 1] >= target:
                index = i
                break
        
        if index == -1:
            return False
        
        # Step 2: Binary search in that row
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False


# ✅ Test Case 1 (Target Present)
# matrix = [
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,60]
# ]
# target = 3
# Output: True

# ✅ Test Case 2 (Target Not Present)
# target = 13
# Output: False

# ✅ Test Case 3 (Last Element)
# target = 60
# Output: True

# ✅ Test Case 4 (First Element)
# target = 1
# Output: True