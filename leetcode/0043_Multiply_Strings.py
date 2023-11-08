"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 
Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    # def multiply(self, num1: str, num2: str) -> str:
    def multiply(self, num1, num2):
        ans = ""
        new_line = ""
        previous_line = ""
        remain = 0
        length1 = len(num1)
        length2 = len(num2)
        
        if num1 == "0" or num2 == "0":
            return "0"

        for index1 in (range(length1)):
            for index2 in (range(length2)):
                if previous_line:
                    remain += int(previous_line[-1])
                    previous_line = previous_line[:-1]
                    
                calc = int(num1[-index1 - 1]) * int(num2[-index2 - 1]) + remain
                remain = calc // 10
                new_line = str(calc % 10) + new_line
                
                if remain and index2 == length2 - 1:
                    new_line = str(remain) + new_line
            
            ans = new_line[-1] + ans
            previous_line = new_line[:-1]
            new_line = ""
            remain = 0
        
        ans = previous_line + ans
        
        return ans


def main():
    num1 = "123"
    num2 = "456"

    solution = Solution()

    result = solution.multiply(num1, num2)
    
    print(result)


if __name__ == "__main__":
    main()