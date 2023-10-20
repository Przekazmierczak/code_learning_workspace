"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
Constraints:

1 <= n <= 8
"""

class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    def generateParenthesis(self, n):
              
        def add_para(open_p, close_p, current, result):
            if open_p == 0 and close_p == 0:
                ans.append(current)
                return 
            
            if open_p > 0:
                add_para(open_p - 1, close_p, current + "(", result)
                            
            if open_p < close_p:
                add_para(open_p, close_p - 1, current + ")", result)
        
        open_p = n
        close_p = n
        current = ""
        ans = []
        
        add_para(open_p, close_p, current, ans)
        
        return ans



def main():
    n = 3

    solution = Solution()

    result = solution.generateParenthesis(n)
    
    print(result)


if __name__ == "__main__":
    main()