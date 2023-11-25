"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        longest = 0
        currest_longest = 0
        unique = set()

        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                currest_longest += 1
                longest = max(currest_longest, longest)
                right += 1
                
            else:
                unique.remove(s[left])
                currest_longest -= 1
                left += 1

        return longest
            

def main():
    s = "abcabcbb"

    solution = Solution()

    result = solution.lengthOfLongestSubstring(s)
    
    print(result)


if __name__ == "__main__":
    main()