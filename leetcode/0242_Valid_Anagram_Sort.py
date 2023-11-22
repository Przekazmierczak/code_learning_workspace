"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        return False

def main():
    s = "anagram"
    t = "nagaram"

    solution = Solution()

    result = solution.isAnagram(s, t)
    
    print(result)


if __name__ == "__main__":
    main()