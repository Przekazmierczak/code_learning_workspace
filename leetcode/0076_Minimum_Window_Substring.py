"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution:
    def minWindow(self, s, t):
        letters = {}
        
        for letter in t:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        
        left, right = 0, 0
        check = len(letters)
        length = float("inf")
        ans = (0, -1)
        
        while right < len(s):
            if s[right] in letters:
                letters[s[right]] -= 1
                if letters[s[right]] == 0:
                    check -= 1

            while check == 0:
                if right - left + 1 < length:
                    length = right - left + 1
                    ans = (left, right)

                if s[left] in letters:
                    letters[s[left]] += 1
                    if letters[s[left]] > 0:
                        check += 1

                left += 1

            right += 1
      
        return(s[ans[0]:ans[1] + 1])

def main():
    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"

    solution = Solution()

    result = solution.minWindow(s, t)
    
    print(result)


if __name__ == "__main__":
    main()