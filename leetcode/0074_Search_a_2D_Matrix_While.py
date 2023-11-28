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
        column_size = len(matrix)
        row_size = len(matrix[0])

        left = 0
        right = column_size - 1
        row = -1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][row_size - 1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        if row > -1:
            left = 0
            right = row_size - 1

            while left <= right:
                mid = (left + right) // 2

                if matrix[row][mid] > target:
                    right = mid - 1
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    return True
                
        return False
    

def main():
    matrix = [[1],[3]]
    target = 3

    solution = Solution()

    result = solution.searchMatrix(matrix, target)
    
    print(result)


if __name__ == "__main__":
    main()