"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

class Solution:
    # def decodeString(self, s: str) -> str:
    def decodeString(self, s):
        stack = []
        para = {}
        
        for i in range(len(s)):
            if s[i] == "[":
                stack.append(i)
            elif s[i] == "]":
                j = stack.pop()
                para[j] = i
        
        def decode(num, index1, index2):
            curr = ""
            while index1 <= index2:
                if s[index1].isnumeric():
                    curr_num = ""
                    while s[index1].isnumeric():
                        curr_num += s[index1]
                        index1 += 1
                    close = para[index1]
                    curr += decode(int(curr_num), index1 + 1, close - 1)
                    index1 = close + 1
                else:
                    curr += s[index1]
                    index1 += 1
            return curr * num
        
        return decode(1, 0, len(s) - 1)
            

def main():
    s = "2[abc]3[cd]ef"

    solution = Solution()

    result = solution.decodeString(s)
    
    print(result)


if __name__ == "__main__":
    main()