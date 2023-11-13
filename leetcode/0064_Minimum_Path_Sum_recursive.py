"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
"""
class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        memory = [[-1 for _ in range(n)] for _ in range(m)]

        def move(position_m, position_n):
            
            if position_m >= m or position_n >= n:
                return float("inf")
            
            if memory[position_m][position_n] != -1:
                return memory[position_m][position_n]
                
            if position_m == m - 1 and position_n == n - 1:
                return grid[position_m][position_n]
            
            new_sum = min(move(position_m + 1, position_n), move(position_m, position_n + 1)) + grid[position_m][position_n]
            memory[position_m][position_n] = new_sum
            return new_sum
        
        return move(0, 0)


def main():
    grid = [[1,3,1],[1,5,1],[4,2,1]]

    solution = Solution()

    result = solution.minPathSum(grid)
    
    print(result)


if __name__ == "__main__":
    main()