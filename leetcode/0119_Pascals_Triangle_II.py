"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
"""

class Solution:
    # def generate(self, numRows: int) -> List[List[int]]:
    def getRow(self, rowIndex):
        def generate_row(previous_row):
            new_row = [1]

            for i in range(len(previous_row)):
                new_row.append(sum(previous_row[i:i + 2]))

            return new_row
        
        row = []
        
        for _ in range(rowIndex + 1):
            row = generate_row(row)
        return row
            

def main():
    rowIndex = 3

    solution = Solution()

    result = solution.getRow(rowIndex)
    
    print(result)


if __name__ == "__main__":
    main()