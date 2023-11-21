"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 
Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""

class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    def minimumTotal(self, triangle):
        def check(row, pointer):
            if row == len(triangle):
                return 0
            
            if (row, pointer) in memo:
                return memo[(row, pointer)]
            
            left = check(row + 1, pointer)
            right = check(row + 1, pointer + 1)
            
            memo[(row, pointer)] = min(left, right) + triangle[row][pointer]
            
            return memo[(row, pointer)]
        
        memo = {}
        return check(0, 0)
            

def main():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

    solution = Solution()

    result = solution.minimumTotal(triangle)
    
    print(result)


if __name__ == "__main__":
    main()