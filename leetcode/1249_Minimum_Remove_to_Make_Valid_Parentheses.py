"""
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""

class Solution:
    # def minRemoveToMakeValid(self, s: str) -> str:
    def minRemoveToMakeValid(self, s):
        opens = []
        to_remove = []
        res = ""
        
        for i in range(len(s)):
            if s[i] == "(":
                opens.append(i)
            elif s[i] == ")":
                if opens:
                    opens.pop()
                else:
                    to_remove.append(i)
        to_remove.extend(opens)
        to_remove = set(to_remove)
        
        for i in range(len(s)):
            if i not in to_remove:
                res += s[i]
        return res
            

def main():
    s = "lee(t(c)o)de)"

    solution = Solution()

    result = solution.minRemoveToMakeValid(s)
    
    print(result)


if __name__ == "__main__":
    main()