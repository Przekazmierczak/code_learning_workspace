"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

class Solution:
    # def wordPattern(self, pattern: str, s: str) -> bool:
    def wordPattern(self, pattern, s):
        array = s.split()
        pattern_dict = {}
        array_dict = {}
        
        if len(pattern) != len(array):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = array[i]
            elif pattern_dict[pattern[i]] != array[i]:
                return False
            
            if array[i] not in array_dict:
                array_dict[array[i]] = pattern[i]
            elif array_dict[array[i]] != pattern[i]:
                return False
            
        return True
            

def main():
    pattern = "abba"
    s = "dog cat cat dog"

    solution = Solution()

    result = solution.wordPattern(pattern, s)
    
    print(result)


if __name__ == "__main__":
    main()