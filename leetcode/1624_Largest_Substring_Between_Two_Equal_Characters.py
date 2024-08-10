"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
"""

class Solution:
    # def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    def maxLengthBetweenEqualCharacters(self, s):
        memo = {}
        res = -1
        
        for i, l in enumerate(s):
            if l in memo:
                res = max(res, i - memo[l] - 1)
            else:
                memo[l] = i
        
        return res
            

def main():
    s = "abca"

    solution = Solution()

    result = solution.maxLengthBetweenEqualCharacters(s)
    
    print(result)


if __name__ == "__main__":
    main()