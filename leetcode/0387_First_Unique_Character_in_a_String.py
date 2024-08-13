"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

class Solution:
    # def firstUniqChar(self, s: str) -> int:
    def firstUniqChar(self, s):
        memo = {}
        
        for l in s:
            if l not in memo:
                memo[l] = 0
            memo[l] += 1
            
        for i, l in enumerate(s):
            if memo[l] == 1:
                return i
        
        return - 1
            

def main():
    s = "loveleetcode"

    solution = Solution()

    result = solution.firstUniqChar(s)
    
    print(result)


if __name__ == "__main__":
    main()