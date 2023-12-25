"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

class Solution:
    # def numDistinct(self, s: str, t: str) -> int:
    def numDistinct(self, s, t):
        memo = {}
        LENS = len(s)
        LENT = len(t)

        def dfs(ps, pt):
            if pt == LENT:
                return 1
            
            if ps == LENS or LENT - pt > LENS - ps:
                return 0
            
            if (ps, pt) in memo:
                return memo[(ps, pt)]
            
            value = 0

            if s[ps] == t[pt]:
                value += dfs(ps + 1, pt + 1)
            value += dfs(ps + 1, pt)
            
            memo[(ps, pt)] = value

            return value
        
        return dfs(0, 0)

def main():
    # s = "rabbbit"
    # t = "rabbit"
    s = "babgbag"
    t = "bag"

    solution = Solution()

    result = solution.numDistinct(s, t)
    
    print(result)


if __name__ == "__main__":
    main()