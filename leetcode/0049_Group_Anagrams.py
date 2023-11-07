"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 
Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        new_strs = []
        for word in strs:
            new_word = sorted(word)
            new_strs.append((new_word, word))
        
        new_strs.sort()

        ans = []
        for index in range(len(new_strs)):
            if index > 0 and new_strs[index][0] == new_strs[index - 1][0]:
                ans[-1].append(new_strs[index][1])
            else:
                ans.append([new_strs[index][1]])
                
        return ans


def main():
    strs = ["eat","tea","tan","ate","nat","bat"]

    solution = Solution()

    result = solution.groupAnagrams(strs)
    
    print(result)


if __name__ == "__main__":
    main()