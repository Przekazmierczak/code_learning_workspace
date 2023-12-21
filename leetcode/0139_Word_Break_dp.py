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

class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def wordBreak(self, s, wordDict):
        substrings = set()

        for word in wordDict:
            if s.startswith(word):
                substrings.add(s[len(word):])

        while substrings:
            add_list = []
            remove_list = []
            for check in substrings:
                if check == "":
                    return True
                for word in wordDict:
                    if check.startswith(word):
                        add_list.append(check[len(word):])
                remove_list.append(check)

            for add_ele in add_list:
                substrings.add(add_ele)
            for remove_ele in remove_list:
                substrings.remove(remove_ele)
        return False


def main():
    s = "applepenapple"
    wordDict = ["apple","pen"]

    solution = Solution()

    result = solution.wordBreak(s, wordDict)
    
    print(result)


if __name__ == "__main__":
    main()