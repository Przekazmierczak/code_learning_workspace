"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    def ladderLength(self, beginWord, endWord, wordList):
        graph = {}
        visit = set()
        shortest = [float("inf")]

        def check(word1, word2):
            diff = 0
            pointer = 0
            while pointer < len(word1):
                if word1[pointer] != word2[pointer]:
                    diff += 1
                    if diff > 1:
                        break
                pointer += 1
            if diff == 1:
                return True
            return False
        
        def find_end_word(curr, end, path):
            if curr in visit or path >= shortest[0]:
                return
            
            if curr == end:
                shortest[0] = min(path, shortest[0])
                return

            visit.add(curr)
            for next in graph[curr]:
                find_end_word(next, end, path + 1)
            visit.remove(curr)

        for word in wordList:
            graph[word] = set()
            for edge in wordList:
                if check(word, edge):
                    graph[word].add(edge)

        for word in graph:
            if check(beginWord, word):
                find_end_word(word, endWord, 2)

        result = shortest[0] if shortest[0] != float("inf") else 0
        return result

def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution = Solution()

    result = solution.ladderLength(beginWord, endWord, wordList)
    
    print(result)


if __name__ == "__main__":
    main()