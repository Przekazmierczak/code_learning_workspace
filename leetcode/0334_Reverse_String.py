"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

class Solution:
    # def reverseString(self, s) -> None:
    def reverseString(self, s):

        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return s
            

def main():
    s = ["h","e","l","l","o"]

    solution = Solution()

    result = solution.reverseString(s)
    
    print(result)


if __name__ == "__main__":
    main()