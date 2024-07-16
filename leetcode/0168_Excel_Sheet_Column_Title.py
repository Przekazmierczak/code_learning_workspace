"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"

Constraints:

1 <= columnNumber <= 231 - 1
"""

class Solution:
    # def convertToTitle(self, columnNumber: int) -> str:
    def convertToTitle(self, columnNumber):
        res = ""
        while columnNumber > 26:
            rest = columnNumber % 26
            if rest == 0:
                rest = 26
            res = chr(rest + 64) + res
            columnNumber = (columnNumber - rest) // 26
            
        return chr(columnNumber + 64) + res
            

def main():
    columnNumber = 701

    solution = Solution()

    result = solution.convertToTitle(columnNumber)
    
    print(result)


if __name__ == "__main__":
    main()