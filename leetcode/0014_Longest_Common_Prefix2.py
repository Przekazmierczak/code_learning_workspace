"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs):
        i = 0
        res = ""
        curr = None
        while True:
            for s in strs:
                if i < len(s) and not curr:
                    curr = s[i]
                else:
                    if i >= len(s) or curr != s[i]:
                        return res
            res += s[i]
            curr = None
            i += 1

def main():
    strs = ["cir","car"]

    solution = Solution()

    result = solution.longestCommonPrefix(strs)
    
    print(result)


if __name__ == "__main__":
    main()