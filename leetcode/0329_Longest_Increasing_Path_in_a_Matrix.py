"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""

class Solution:
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    def longestIncreasingPath(self, matrix):
        memo ={}
        m = len(matrix)
        n = len(matrix[0])
        result = [0]

        def check_length(pm, pn, prev_value):
            if pm < 0 or pm >= m or pn < 0 or pn >= n or prev_value >= matrix[pm][pn]:
                return 0
            
            if (pm, pn) in memo:
                return memo[(pm, pn)]
            
            value = max(1 + check_length(pm - 1, pn, matrix[pm][pn]), 1 + check_length(pm + 1, pn, matrix[pm][pn]), 1 + check_length(pm, pn - 1, matrix[pm][pn]), 1 + check_length(pm, pn + 1, matrix[pm][pn]))
            
            memo[(pm, pn)] = value
            result[0] = max(result[0], value)
            
            return value
        
        for i in range(m):
            for j in range(n):
                check_length(i, j, -1)
        
        return result[0]

def main():
    matrix = [[9,9,4],[6,6,8],[2,1,1]]

    solution = Solution()

    result = solution.longestIncreasingPath(matrix)
    
    print(result)


if __name__ == "__main__":
    main()