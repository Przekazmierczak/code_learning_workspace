"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 
Constraints:

1 <= n <= 20
"""

class Solution:
    # def generateMatrix(self, n: int) -> List[List[int]]:
    def generateMatrix(self, n):
        matrix = []
        for _ in range(n):
            matrix.append([0] * n)

        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        number = 1

        while number <= n * n:
            for index in range(left, right + 1):
                matrix[top][index] = number
                number += 1
            top += 1

            for index in range(top, bottom + 1):
                matrix[index][right] = number
                number += 1
            right -= 1

            for index in range(right, left - 1, -1):
                matrix[bottom][index] = number
                number += 1
            bottom -= 1

            for index in range(bottom, top - 1, -1):
                matrix[index][left] = number
                number += 1
            left += 1
        
        return matrix

def main():
    n = 10

    solution = Solution()

    result = solution.generateMatrix(n)
    
    print(result)


if __name__ == "__main__":
    main()