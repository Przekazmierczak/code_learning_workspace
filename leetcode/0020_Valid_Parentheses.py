"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    # def isValid(self, s: str) -> bool:
    def isValid(self, s):
        dic = {"(": ")", "[": "]", "{": "}"}
        
        close = []
        
        for c in s:
            if c in dic.keys():
                close.append(dic[c])
            elif c in dic.values():
                if close != []:
                    if c != close.pop():
                        return False
                else:
                    return False
                
        if close == []:
            return True


def main():
    s = "()[]{}"

    solution = Solution()

    result = solution.isValid(s)
    
    print(result)


if __name__ == "__main__":
    main()