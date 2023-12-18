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
from collections import deque

class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    def ladderLength(self, beginWord, endWord, wordList):
        graph  = {}
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in graph:
                    graph[pattern] = []
                graph[pattern].append(word)

        visit = set()
        que = deque([beginWord])
        shortest = 1

        while que:
            for i in range(len(que)):
                word = que.popleft()
                if word == endWord:
                    return shortest

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbor_word in graph[pattern]:
                        if neighbor_word in graph[pattern]:
                            if neighbor_word not in visit:
                                visit.add(neighbor_word)
                                que.append(neighbor_word)
            shortest += 1
        
        return 0
def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution = Solution()

    result = solution.ladderLength(beginWord, endWord, wordList)
    
    print(result)


if __name__ == "__main__":
    main()