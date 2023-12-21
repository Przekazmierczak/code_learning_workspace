"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from functools import lru_cache

class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def wordBreak(self, s, wordDict):
        @lru_cache(None)
        def check(index, word_index, word):
            if index == len(s) and word_index == len(word):
                return True
            
            elif index == len(s) and word_index != len(word):
                return False
            
            if word_index == len(word):
                for curr_word in wordDict:
                    if curr_word[0] == s[index]:
                        if check(index + 1, 1, curr_word):
                            return True
                return False
                    
            elif s[index] == word[word_index]:
                if check(index + 1, word_index + 1, word):
                    return True
                return False
            
            elif s[index] != word[word_index]:
                return False
            
        return check(0, 0, "")
                


def main():
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]

    solution = Solution()

    result = solution.wordBreak(s, wordDict)
    
    print(result)


if __name__ == "__main__":
    main()