"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 
Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""

class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    def longestValidParentheses(self, s):
        open = []
        result = []
        for index, element in enumerate(s):
            if element == "(":
                open.append(index)
                result.append(0)
            else:
                if len(open) > 0:
                    result.append(1)
                    correct = open.pop()
                    result[correct] = 1
                else:
                    result.append(0)
        
        current_max = 0
        max = 0
        for element in result:
            if element:
                current_max += 1
                if current_max > max:
                    max = current_max
            else:
                current_max = 0
        
        return max



def main():
    s = "()())()()())())())"

    solution = Solution()

    result = solution.longestValidParentheses(s)
    
    print(result)


if __name__ == "__main__":
    main()