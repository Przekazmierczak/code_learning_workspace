"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""

class Solution:
    # def minFlipsMonoIncr(self, s: str) -> int:
    def minFlipsMonoIncr(self, s):
        memo = {}
        def dfs(i, can_zero):
            if i == len(s):
                return 0
            if (i, can_zero) in memo:
                return memo[(i, can_zero)]
            res = float("inf")
            if s[i] == "0":
                if can_zero:
                    res = min(dfs(i + 1, True), res)
                res = min(dfs(i + 1, False) + 1, res)
            else:
                if can_zero:
                    res = min(dfs(i + 1, True) + 1, res)
                res = min(dfs(i + 1, False), res)
            memo[(i, can_zero)] = res
            return res
        return dfs(0, True)
            

def main():
    s = "00110"

    solution = Solution()

    result = solution.minFlipsMonoIncr(s)
    
    print(result)


if __name__ == "__main__":
    main()