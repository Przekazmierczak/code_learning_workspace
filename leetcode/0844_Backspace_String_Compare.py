"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 
Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 
Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    # def backspaceCompare(self, s: str, t: str) -> bool:
    def backspaceCompare(self, s, t):
        pointer_s = len(s) - 1
        pointer_t = len(t) - 1
        
        while True:
            if pointer_s >= 0 and s[pointer_s] == "#":
                pointer_s -= 1
                back = 1
                while back:
                    if pointer_s >= 0 and s[pointer_s] == "#":
                        back += 1
                    else:
                        back -= 1
                    pointer_s -= 1
            
            elif pointer_t >= 0 and t[pointer_t] == "#":
                pointer_t -= 1
                back = 1
                while back:
                    if pointer_t  >= 0 and t[pointer_t] == "#":
                        back += 1
                    else:
                        back -= 1
                    pointer_t -= 1
            
            elif pointer_s < 0 and pointer_t < 0:
                return True
            
            elif pointer_s < 0 or pointer_t < 0 or s[pointer_s] != t[pointer_t]:
                return False
            
            else:
                pointer_s -= 1
                pointer_t -= 1
            

def main():
    s = "ab##"
    t = "c#d#"

    solution = Solution()

    result = solution.backspaceCompare(s, t)
    
    print(result)


if __name__ == "__main__":
    main()