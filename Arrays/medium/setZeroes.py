class Solution:
    def setZeroes(self, matrix):
        rows = set()
        cols = set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Step 1: Find zero positions
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Step 2: Set rows and columns to zero
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

# how it works
# 💡 Idea:
# Traverse matrix → store row and column indices where 0 appears
# Traverse again → make those rows & columns zero



# ✅ Test Case 1
# matrix = [
#     [1,1,1],
#     [1,0,1],
#     [1,1,1]
# ]
# Output:
# [
#  [1,0,1],
#  [0,0,0],
#  [1,0,1]
# ]

# ✅ Test Case 2
# matrix = [
#     [0,1,2,0],
#     [3,4,5,2],
#     [1,3,1,5]
# ]
# Output:
# [
#  [0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]
# ]