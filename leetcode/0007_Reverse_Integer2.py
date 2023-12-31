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
        MAX = 2147483647
        MIN = 2147483648

        sign = 1 if x >= 0 else - 1
        result = 0
        x = abs(x)

        while x:
            new_digit = x % 10
            x = x // 10

            if result > MAX // 10 or (sign == 1 and result == MAX // 10 and new_digit >= MAX % 10) or (sign == -1 and result == MIN // 10 and new_digit >= MIN % 10):
                return 0

            result = result * 10 + new_digit
        
        return result * sign



def main():
    x = 7463847412

    solution = Solution()

    result = solution.reverse(x)
    
    print(result)


if __name__ == "__main__":
    main()