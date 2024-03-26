"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'
"""

class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    def findRepeatedDnaSequences(self, s):
        set1 = set()
        set2 = set()
        l, r = 0, 10
        
        while r < len(s) + 1:
            curr = s[l:r]
            if curr in set1:
                set2.add(curr)
            else:
                set1.add(curr)
            l += 1
            r += 1
        
        return set2
            

def main():
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

    solution = Solution()

    result = solution.findRepeatedDnaSequences(s)
    
    print(result)


if __name__ == "__main__":
    main()