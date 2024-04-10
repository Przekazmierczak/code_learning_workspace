"""
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:

1 <= num <= 231 - 1
"""

class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        
        l, r = 0, num // 2
        
        while l <= r:
            mid = (l + r) // 2
            sqrt = mid * mid
            
            if sqrt == num:
                return True
            elif sqrt > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

def main():
    num = 16

    solution = Solution()

    result = solution.isPerfectSquare(num)
    
    print(result)


if __name__ == "__main__":
    main()