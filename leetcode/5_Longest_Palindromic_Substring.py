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
        longest_string = ""
        longest_string_len = 0

        for _ in s:
            for i in range(2):
                # Odd length palindromic substring
                if i == 0:
                    left_pointer = main_pointer - 1
                    right_pointer = main_pointer + 1
                    string = s[main_pointer]
                # Even length palindromic substring
                else:
                    left_pointer = main_pointer
                    right_pointer = main_pointer + 1
                    string = ""

                while True:
                    # Pointer reaches the end of the 's' string.
                    if left_pointer < 0 or right_pointer > (len(s) - 1):
                        if len(string) > longest_string_len:
                            longest_string = string
                            longest_string_len = len(longest_string)
                        break
                    # Characters match.
                    elif s[left_pointer] != s[right_pointer]:
                        if len(string) > longest_string_len:
                            longest_string = string
                            longest_string_len = len(longest_string)
                        break
                    # Characters are different.   
                    else:
                        string = s[left_pointer] + string + s[right_pointer]

                        left_pointer -= 1
                        right_pointer += 1

            main_pointer += 1
        return longest_string


def main():
    s = "babad"

    solution = Solution()

    result = solution.longestPalindrome(s)
    
    print(result)


if __name__ == "__main__":
    main()