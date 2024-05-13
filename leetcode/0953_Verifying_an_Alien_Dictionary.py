"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

class Solution:
    # def isAlienSorted(self, words: List[str], order: str) -> bool:
    def isAlienSorted(self, words, order):
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
            
        def check(word1, word2):
            for i in range(len(word1)):
                if i == len(word2) or dic[word1[i]] > dic[word2[i]]:
                    return False
                elif dic[word1[i]] < dic[word2[i]]:
                    return True
            return True
        
        for i in range(1, len(words)):
            if not check(words[i - 1], words[i]):
                return False
        return True
            

def main():
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"

    solution = Solution()

    result = solution.isAlienSorted(words, order)
    
    print(result)


if __name__ == "__main__":
    main()