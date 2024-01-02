"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:
    # def validPalindrome(self, s: str) -> bool:
    def validPalindrome(self, s):
        def match(left, right, skipped):
            if left >= right:
                return True
            
            if s[left] != s[right] and skipped:
                return False
            
            elif s[left] != s[right]:
                return match(left + 1, right, True) or match(left, right -1, True)
            else:
                return match(left + 1, right - 1, skipped)
        
        return match(0, len(s) - 1, False)
        

def main():
    s = "aba"

    solution = Solution()

    result = solution.validPalindrome(s)
    
    print(result)


if __name__ == "__main__":
    main()