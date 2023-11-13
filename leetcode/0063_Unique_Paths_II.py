"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 
Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, obstacleGrid):
        memory = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        def move(position_m, position_n):
            if (position_m, position_n) in memory:
                return memory[(position_m, position_n)]
            
            if position_m >= m or position_n >= n:
                return 0
            
            if obstacleGrid[position_m][position_n] == 1:
                return 0
            
            if position_m == m - 1 and position_n == n - 1:
                return 1
            
            new_position = move(position_m + 1, position_n) + move(position_m, position_n + 1)
            memory[(position_m, position_n)] = new_position
            return new_position
        
        return move(0, 0)

def main():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

    solution = Solution()

    result = solution.uniquePathsWithObstacles(obstacleGrid)
    
    print(result)


if __name__ == "__main__":
    main()