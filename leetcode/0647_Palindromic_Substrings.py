"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s):
        main_pointer = 0
        counter = 0

        for _ in s:
            counter += 1
            for i in range(2):
                # Odd length palindromic substring
                if i == 0:
                    left_pointer = main_pointer - 1
                    right_pointer = main_pointer + 1
                # Even length palindromic substring
                else:
                    left_pointer = main_pointer
                    right_pointer = main_pointer + 1

                while True:
                    # Characters match and pointer in 's' string range.
                    if left_pointer >= 0 and right_pointer < (len(s)) and s[left_pointer] == s[right_pointer]:
                        counter += 1
                        left_pointer -= 1
                        right_pointer += 1
                    # Characters are different.   
                    else:
                        break
            main_pointer += 1

        return counter

def main():
    s = "aaa"

    solution = Solution()

    result = solution.longestPalindrome(s)
    
    print(result)


if __name__ == "__main__":
    main()