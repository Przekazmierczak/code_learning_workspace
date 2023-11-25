"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 
Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    def characterReplacement(self, s, k):
        max_length = 0
        left = 0
        right = 0
        dic = {}

        while right < len(s):
            if s[right] in dic:
                dic[s[right]] += 1
            else:
                dic[s[right]] = 1

            max_dic = max(dic.values())

            if (right - left + 1) > max_dic + k:
                dic[s[left]] -= 1
                left += 1

            max_length = max(right - left + 1, max_length)
            right += 1

        return max_length


def main():
    s = "AABABBA"
    k = 1

    solution = Solution()

    result = solution.characterReplacement(s, k)
    
    print(result)


if __name__ == "__main__":
    main()