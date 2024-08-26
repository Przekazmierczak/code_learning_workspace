"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
"""

class Solution:
    # def frequencySort(self, s: str) -> str:
    def frequencySort(self, s):
        res = []
        letters = {}
        max_freq = 0
        
        for l in s:
            if l not in letters:
                letters[l] = 0
            letters[l] += 1
            max_freq = max(max_freq, letters[l])
        
        count = [[] for _ in range(max_freq + 1)]
        for key in letters:
            count[letters[key]].append(key)
        
        for i in range(len(count) - 1, 0, -1):
            if count[i]:
                for letter in count[i]:
                    res.append(letter * i)
        
        return "".join(res)
            

def main():
    s = "Aabb"

    solution = Solution()

    result = solution.frequencySort(s)
    
    print(result)


if __name__ == "__main__":
    main()