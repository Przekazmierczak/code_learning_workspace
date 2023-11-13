"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 
Constraints:

1 <= m, n <= 100
"""
class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    def uniquePaths(self, m, n):
        memory = {}
        
        def move(position_m, position_n):
            if (position_m, position_n) in memory:
                return memory[(position_m, position_n)]
            
            if position_m >= m or position_n >= n:
                return 0
            
            if position_m == m - 1 and position_n == n - 1:
                return 1
            
            new_position = move(position_m + 1, position_n) + move(position_m, position_n + 1)
            memory[(position_m, position_n)] = new_position
            return new_position
        
        return move(0, 0)

def main():
    m = 3
    n = 7

    solution = Solution()

    result = solution.uniquePaths(m, n)
    
    print(result)


if __name__ == "__main__":
    main()