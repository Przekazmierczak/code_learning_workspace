"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""

class Solution:
    # def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    def arrayStringsAreEqual(self, word1, word2):
        row1, col1 = 0, 0
        row2, col2 = 0, 0
        
        last_row1 = len(word1)
        last_row2 = len(word2)
        
        while True:
            if row1 == last_row1 and row2 == last_row2:
                return True
            
            if row1 == last_row1 or row2 == last_row2 or word1[row1][col1] != word2[row2][col2]:
                return False
            
            if col1 < len(word1[row1]) - 1:
                col1 += 1
            else:
                row1 += 1
                col1 = 0
            
            if col2 < len(word2[row2]) - 1:
                col2 += 1
            else:
                row2 += 1
                col2 = 0
            

def main():
    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]

    solution = Solution()

    result = solution.arrayStringsAreEqual(word1, word2)
    
    print(result)


if __name__ == "__main__":
    main()