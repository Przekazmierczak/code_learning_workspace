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
from functools import lru_cache 

class Solution:
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    def isInterleave(self, s1, s2, s3):
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        
        @lru_cache(None)
        def check(p_s1, p_s2, p_s3, len_s1, len_s2, len_s3):
            s1_correct, s2_correct = False, False

            if p_s1 == len_s1 and p_s2 == len_s2:
                return True
            
            if ((p_s1 < len_s1 and s1[p_s1] != s3[p_s3]) and (p_s2 < len_s2 and s2[p_s2] != s3[p_s3])):
                return False
            
            if p_s1 < len_s1 and s1[p_s1] == s3[p_s3]:
                s1_correct = check(p_s1 + 1, p_s2, p_s3 + 1, len_s1, len_s2, len_s3)
                
            if p_s2 < len_s2 and s2[p_s2] == s3[p_s3]:
                s2_correct = check(p_s1, p_s2 + 1, p_s3 + 1, len_s1, len_s2, len_s3)
            
            return s1_correct or s2_correct
        
        return check(0, 0, 0, len_s1, len_s2, len_s3)
def main():
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

    solution = Solution()

    result = solution.isInterleave(s1, s2, s3)
    
    print(result)


if __name__ == "__main__":
    main()