"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

class Solution:
    # def reverseWords(self, s: str) -> str:
    def reverseWords(self, s):
        res = list(s)
        res.append(" ")
        l, r = -1, 0
        
        while l < len(s):
            while res[r] != " ":
                r += 1
            
            curr_r = r - 1
            curr_l = l + 1
            while curr_l < curr_r:
                res[curr_l], res[curr_r] = res[curr_r], res[curr_l]
                curr_l += 1
                curr_r -= 1
            
            l = r
            r += 1
        
        res.pop()
        
        return "".join(res)
            

def main():
    s = "Let's take LeetCode contest"

    solution = Solution()

    result = solution.reverseWords(s)
    
    print(result)


if __name__ == "__main__":
    main()