"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

class Solution:
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    def mergeAlternately(self, word1, word2):
        len1, len2 = len(word1), len(word2)

        i1, i2 = 0, 0
        res = ""
        
        while i1 < len1 and i2 < len2:
            res += word1[i1]
            i1 += 1
            res += word2[i2]
            i2 += 1
        
        while i1 < len1:
            res += word1[i1]
            i1 += 1
        
        while i2 < len2:
            res += word2[i2]
            i2 += 1
        
        return res
            

def main():
    word1 = "abcd"
    word2 = "pq"

    solution = Solution()

    result = solution.mergeAlternately(word1, word2)
    
    print(result)


if __name__ == "__main__":
    main()