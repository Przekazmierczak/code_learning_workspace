"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
"""

class Solution:
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    def isInterleave(self, s1, s2, s3):
        LEN1, LEN2, LEN3 = len(s1), len(s2), len(s3)

        if LEN1 + LEN2 != LEN3:
            return False
        
        dp = [[False for _ in range(LEN2 + 1)] for _ in range(LEN1 + 1)]
        dp[0][0] = True

        for i in range(LEN1 + 1):
            for j in range(LEN2 + 1):

                if (i > 0 and s1[i - 1] == s3[i + j - 1]) and dp[i - 1][j]:
                    dp[i][j] = True
                elif (j > 0 and s2[j - 1] == s3[i + j - 1]) and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[-1][-1]

def main():
    s1 = "a"
    s2 = ""
    s3 = "c"

    solution = Solution()

    result = solution.isInterleave(s1, s2, s3)
    
    print(result)


if __name__ == "__main__":
    main()