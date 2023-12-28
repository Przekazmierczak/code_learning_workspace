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
        open_para, star = [], []

        for index, parenthesis in enumerate(s):
            if parenthesis == "(":
                open_para.append(index)
            elif parenthesis == "*":
                star.append(index)
            else:
                if open_para:
                    open_para.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while open_para:
            if star:
                curr_open = open_para.pop()
                curr_star = star.pop()
                if curr_open > curr_star:
                    return False
            else: 
                return False

        return True


def main():
    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

    solution = Solution()

    result = solution.checkValidString(s)
    
    print(result)


if __name__ == "__main__":
    main()