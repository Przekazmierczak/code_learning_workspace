"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    def strStr(self, haystack, needle):
        max_pointer = len(needle)
        failure_table = []
        
        for _ in range(len(needle)):
            failure_table.append(0)

        j = 0
        for i in range(1, len(failure_table)):
            while j > 0 and needle[j] != needle[i]:
                j = failure_table[j - 1]
            if needle[j] == needle[i]:
                j += 1
            failure_table[i] = j

        j = 0
        for i in range(len(haystack)):
            while j> 0 and needle[j] != haystack[i]:
                j = failure_table[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == max_pointer:
                return i - j + 1
        
        return -1



def main():
    haystack = "leetcode"
    needle = "leeto"

    solution = Solution()

    result = solution.strStr(haystack, needle)
    
    print(result)


if __name__ == "__main__":
    main()