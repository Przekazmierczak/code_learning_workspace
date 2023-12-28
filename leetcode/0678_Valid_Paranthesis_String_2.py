"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""

class Solution:
    # def checkValidString(self, s: str) -> bool:
    def checkValidString(self, s):
        max_open, min_open = 0, 0

        for para in s:
            if para == "(":
                max_open += 1
                min_open += 1

            elif para == ")":
                max_open -= 1
                min_open -= 1
                
            else:
                max_open += 1
                min_open -= 1

            if max_open < 0:
                return False
            
            if min_open < 0:
                min_open = 0

        return min_open == 0


def main():
    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

    solution = Solution()

    result = solution.checkValidString(s)
    
    print(result)


if __name__ == "__main__":
    main()