"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        matrix = matrix
        result = []
        try:
            while True:
                for i in range(len(matrix[0])):
                    result.append(matrix[0][i])
                matrix.pop(0)

                for i in range(len(matrix)):
                    result.append(matrix[i].pop())

                for i in reversed(range(len(matrix[-1]))):
                    result.append(matrix[-1][i])
                matrix.pop()

                for i in reversed(range(len(matrix))):
                    result.append(matrix[i].pop(0))
        except IndexError:
            return result


def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    solution = Solution()

    result = solution.spiralOrder(matrix)
    
    print(result)


if __name__ == "__main__":
    main()