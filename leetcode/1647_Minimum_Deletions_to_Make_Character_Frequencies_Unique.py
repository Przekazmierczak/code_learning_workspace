"""
A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
"""

class Solution:
    # def minDeletions(self, s: str) -> int:
    def minDeletions(self, s):
        letters = {}
        freq = set()
        res = 0
        
        for l in s:
            if l not in letters:
                letters[l] = 0
            letters[l] += 1
        
        for count in letters.values():
            while count != 0 and count in freq:
                count -= 1
                res += 1
            freq.add(count)
        
        return res
            

def main():
    s = "aaabbbcc"

    solution = Solution()

    result = solution.minDeletions(s)
    
    print(result)


if __name__ == "__main__":
    main()