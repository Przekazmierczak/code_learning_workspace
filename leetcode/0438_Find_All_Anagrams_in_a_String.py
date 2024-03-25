"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    def findAnagrams(self, s, p):
        def check():
            for key in dic:
                if dic[key] != 0:
                    return False
            return True
        
        dic = {}
        l, r = 0, 0
        res = []
        
        for letter in p:
            if letter not in dic:
                dic[letter] = 0
            dic[letter] += 1
        
        while r < len(s):
            if s[r] not in dic:
                dic[s[r]] = 0         
            dic[s[r]] -= 1
            r += 1
            if r >= len(p):
                if check():
                    res.append(l)
                dic[s[l]] += 1
                l += 1

        return res
            

def main():
    s = "cbaebabacd"
    p = "abc"

    solution = Solution()

    result = solution.findAnagrams(s, p)
    
    print(result)


if __name__ == "__main__":
    main()