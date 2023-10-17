"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    def isMatch(self, s, p):
        s_pointer = 0
        p_pointer = 0
        # Dictionary to store already computed results
        memo = {}

        def check(s_pointer, p_pointer):
            # Check if the result is already memoized.
            if (s_pointer, p_pointer) in memo:
                return memo[(s_pointer, p_pointer)]
            
            # If 'p_pointer' reaches the end of the expression, check if 's_pointer' also reached the end of 's'.
            if p_pointer == len(p):
                result = s_pointer == len(s)
            else:
                # Check if the current character in 's' and the current character in 'p' match or if 'p' contains a '.'.
                match = (s_pointer < len(s)) and (s[s_pointer] == p[p_pointer] or p[p_pointer] == '.')
                # If the next character in 'p' is "*", there are two possibilities:
                if p_pointer + 1 < len(p) and p[p_pointer + 1] == '*':
                    # Possibility 1: Move 'p_pointer' two steps forward and check if it's a match.
                    # Possibility 2: If there's a match and the '*' acts as zero or more of the preceding element, move 's_pointer' one step forward and recheck.
                    result = (check(s_pointer, p_pointer + 2) or (match and check(s_pointer + 1, p_pointer)))
                # If 'match' is true, move both 's_pointer' and 'p_pointer' one step forward and recheck.
                else:
                    result = match and check(s_pointer + 1, p_pointer + 1)

            # Save the result for the current state in the memo dictionary.
            memo[(s_pointer, p_pointer)] = result
            # Return the result.
            return result

        return check(s_pointer, p_pointer)
        

def main():
    s = "aaaaaaaaaaaaaaaaaaa"
    p = "a*a*a*a*a*a*a*a*a*"
    solution = Solution()

    result = solution.isMatch(s, p)
    
    print(result)


if __name__ == "__main__":
    main()