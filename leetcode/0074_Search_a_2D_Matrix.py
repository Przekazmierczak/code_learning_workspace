"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        column = len(matrix[0])
        def binary_row(matrix, left, right):
            if right - left == 1:
                if target < matrix[right][0]:
                    return left
                else:
                    return right
                
            mid = (right + left) // 2
            
            if matrix[mid][0] > target:
                return binary_row(matrix, left, mid)
            else:
                return binary_row(matrix, mid, right)
        
        def binary_column(matrix, left, right, row):
            if matrix[row][left] == target or matrix[row][right] == target:
                return True
            if left >= right:
                return False
        
            mid = (right + left) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                return binary_column(matrix, left, mid - 1, row)
            else:
                return binary_column(matrix, mid + 1, right, row)

        if row > 1:
            find_row = binary_row(matrix, 0, row - 1)
        else:
            find_row = 0
        return binary_column(matrix, 0, column -1, find_row)
    

def main():
    matrix = [[1,3,5]]
    target = 3

    solution = Solution()

    result = solution.searchMatrix(matrix, target)
    
    print(result)


if __name__ == "__main__":
    main()