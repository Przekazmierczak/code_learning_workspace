"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:

Input: 
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
Constraints:

0 <= x <= 231 - 1
"""

class Solution:
    # def mySqrt(self, x: int) -> int:
    def mySqrt(self, x):
        l = 0
        r = x
       
        while True:
            half = (l + r) // 2
            if half * half <= x < (half + 1) * (half + 1):
                return half
            elif half * half > x < (half + 1) * (half + 1):
                r = half - 1
            else:
                l = half + 1
        return l


def main():
    x = 8

    solution = Solution()

    result = solution.mySqrt(x)
    
    print(result)


if __name__ == "__main__":
    main()