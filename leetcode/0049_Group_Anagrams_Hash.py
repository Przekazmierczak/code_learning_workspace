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
        ans = []
        dics = {}

        for word in strs:
            letters = [0 for _ in range(26)]

            for letter in word:
                letters[ord(letter) - 97] += 1

            letters_tuple = tuple(letters)

            if letters_tuple in dics:
                dics[letters_tuple].append(word)
            else:
                dics[letters_tuple] = [word]
        for key in dics:
            ans.append(dics[key])

        return ans



def main():
    strs = ["eat","tea","tan","ate","nat","bat"]

    solution = Solution()

    result = solution.groupAnagrams(strs)
    
    print(result)


if __name__ == "__main__":
    main()