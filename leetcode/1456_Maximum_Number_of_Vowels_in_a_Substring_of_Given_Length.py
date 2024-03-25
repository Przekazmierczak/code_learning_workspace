"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""

class Solution:
    # def maxVowels(self, s: str, k: int) -> int:
    def maxVowels(self, s, k):
        vowels = {"a", "e", "i", "o", "u"}
        res, count,l = 0, 0, 0
        for r in range(len(s)):
            if r - l + 1 <= k:
                if s[r] in vowels:
                    count += 1
            else:
                if s[r] in vowels:
                    count += 1
                if s[l] in vowels:
                    count -= 1
                l += 1
            res = max(res, count)
        return res
            

def main():
    s = "abciiidef"
    k = 3

    solution = Solution()

    result = solution.maxVowels(s, k)
    
    print(result)


if __name__ == "__main__":
    main()