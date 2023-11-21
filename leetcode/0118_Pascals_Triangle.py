"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 
Constraints:

1 <= numRows <= 30
"""

class Solution:
    # def generate(self, numRows: int) -> List[List[int]]:
    def generate(self, numRows):
        def generate_row(previous_row):
            new_row = [1]

            for i in range(len(previous_row)):
                new_row.append(sum(previous_row[i:i + 2]))

            return new_row
        
        ans = []
        row = []
        
        for _ in range(numRows):
            row = generate_row(row)
            ans.append(row)
        return ans
            

def main():
    numRows = 5

    solution = Solution()

    result = solution.generate(numRows)
    
    print(result)


if __name__ == "__main__":
    main()