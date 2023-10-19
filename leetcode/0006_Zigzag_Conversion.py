"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 
Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        array = []
        result = ""
        
        for _ in range(numRows):
            array.append([])
        
        pointer = 0
        
        try:
            while True:
                for row in range(numRows):
                    array[row].append(s[pointer])
                    pointer += 1
                
                for column in range(numRows - 2):
                    for row in range(numRows):
                        if row == (numRows - 2) - column:
                            array[row].append(s[pointer])
                            pointer += 1
        
        except IndexError:
            for row in array:
                for letter in row:
                    result += letter
            return result


def main():
    s = "PAYPALISHIRING"
    numRows = 3

    solution = Solution()

    result = solution.convert(s, numRows)
    
    print(result)


if __name__ == "__main__":
    main()