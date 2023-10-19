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
        s = ""

        try:
            for index, letter in enumerate(strs[0]):
                flag = True
                for word in strs:
                    if word[index] != letter:
                        flag = False
                        break
                if flag == True:
                    s += letter
                else:
                    break
        
        except IndexError:
            pass
        
        return s

def main():
    strs = ["cir","car"]

    solution = Solution()

    result = solution.longestCommonPrefix(strs)
    
    print(result)


if __name__ == "__main__":
    main()