"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    # def reverse(self, x: int) -> int:
    def reverse(self, x):
        positive = True
        
        if x < 0:
            positive = False
            x *= -1
        
        string = str(x)
        reverse_string = ""
        
        for c in string:
            reverse_string = c + reverse_string
        
        if positive:
            result = int(reverse_string)
        else:
            result = - int(reverse_string)
        
        if result >= -(2 ** 31) and result <= (2 ** 31) - 1:
            return result
        else:
            return 0


def main():
    x = 123

    solution = Solution()

    result = solution.reverse(x)
    
    print(result)


if __name__ == "__main__":
    main()