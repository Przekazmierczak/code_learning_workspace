"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 
Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    def minDistance(self, word1, word2):
        memo = {}
        def solution(pointer1, pointer2):
            if pointer1 == len(word1):
                return len(word2) - pointer2
            
            if pointer2 == len(word2):
                return len(word1) - pointer1
            
            if (pointer1, pointer2) in memo:
                return memo[(pointer1,pointer2)]

            if word1[pointer1] == word2[pointer2]:
                memo[(pointer1, pointer2)] = solution(pointer1 + 1, pointer2 + 1)
            else:
                insert = 1 + solution(pointer1, pointer2 + 1)
                delete = 1 + solution(pointer1 + 1, pointer2)
                replace = 1 + solution(pointer1 + 1, pointer2 + 1)
            
                memo[(pointer1, pointer2)] = min(insert, delete, replace)

            return memo[(pointer1, pointer2)]
        
        return solution(0 , 0)


        

def main():
    word1 = "ddd"
    word2 = "abbbb"

    solution = Solution()

    result = solution.minDistance(word1, word2)
    
    print(result)


if __name__ == "__main__":
    main()