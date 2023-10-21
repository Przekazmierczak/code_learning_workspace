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
        prefixes_length = []
        to_pop = []

        length = len(haystack)
        needle_len = len(needle)
        
        for i in range(length):
            if haystack[i] == needle[0]:
                prefixes_length.append(0)

            for index, prefix_length in enumerate(prefixes_length):
                if haystack[i] == needle[prefix_length]:
                    prefixes_length[index] += 1
                else:
                    to_pop.append(index)

            if to_pop != []:
                for index in reversed(to_pop):
                    prefixes_length.pop(index)
            to_pop = []

            if prefixes_length != [] and prefixes_length[0] == needle_len:
                return (i + 1)- prefixes_length[0]
        return -1



def main():
    haystack = "aabaaabaaac"
    needle = "aabaaac"
    #"mississippi"
    #"issip"
    #"aabaaabaaac"
    #"aabaaac"

    solution = Solution()

    result = solution.strStr(haystack, needle)
    
    print(result)


if __name__ == "__main__":
    main()