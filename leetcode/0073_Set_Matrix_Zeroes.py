"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 
Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution:
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_contain_zero = False
        column_contain_zero = False

        if any(matrix[i][0] == 0 for i in range(m)):
            row_contain_zero = True
            for i in range(1, m):
                if matrix[i][0] == 0:
                    matrix[i][0] = "_"

        if any(matrix[0][i] == 0 for i in range(n)):
            column_contain_zero = True
            for i in range(1, n):
                if matrix[0][i] == 0:
                    matrix[0][i] = "_"

        for i in range (1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = "_"
                    matrix[0][j] = "_"

        for i in range(1, m):
            if matrix[i][0] == "_":
                for j in range(1, n):
                    matrix[i][j] = 0
                matrix[i][0] = 0
                
        for j in range(1, n):
            if matrix[0][j] == "_":
                for i in range(1, m):
                    matrix[i][j] = 0
                matrix[0][j] = 0

        if row_contain_zero:
            for i in range(m):
                matrix[i][0] = 0

        if column_contain_zero:
            for i in range(n):
                matrix[0][i] = 0
        
        return matrix
    

def main():
    matrix = [[1]]

    solution = Solution()

    result = solution.setZeroes(matrix)
    
    print(result)


if __name__ == "__main__":
    main()