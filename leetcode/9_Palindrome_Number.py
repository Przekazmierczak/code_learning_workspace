"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):
        string = str(x)
        half = len(string) // 2
        
        if len(string) % 2:
            right_pointer = half + 1
            
        else:
            right_pointer = half
            
        left_pointer = half - 1
        
        for i in range(half):
            if string[left_pointer] != string[right_pointer]:
                return False
            left_pointer -= 1
            right_pointer += 1

        return True  


def main():
    x = 121

    solution = Solution()

    result = solution.isPalindrome(x)
    
    print(result)

if __name__ == "__main__":
    main()