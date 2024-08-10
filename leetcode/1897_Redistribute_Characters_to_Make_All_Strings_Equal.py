"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

class Solution:
    # def makeEqual(self, words: List[str]) -> bool:
    def makeEqual(self, words):
        dic = {}
        LEN = len(words)
        for word in words:
            for letter in word:
                if letter not in dic:
                    dic[letter] = 0
                dic[letter] += 1
        
        for letter in dic.keys():
            if dic[letter] % LEN:
                return False
            
        return True
            

def main():
    words = ["ab","a"]

    solution = Solution()

    result = solution.makeEqual(words)
    
    print(result)


if __name__ == "__main__":
    main()