"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5

Constraints:

-1000 <= a, b <= 1000
"""

class Solution:
    # def getSum(self, a: int, b: int) -> int:
    def getSum(self, a, b):
        mask = 0xffffffff
        while b:
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry

        if (a>>31) & 1:
            return ~(a^mask)
    
        return a

            
        
def main():
    a = -11
    b = -11

    solution = Solution()

    result = solution.getSum(a, b)
    
    print(result)


if __name__ == "__main__":
    main()