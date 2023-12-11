"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 
Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""

class Solution:
    # def partition(self, s: str) -> List[List[str]]:
    def partition(self, s):
        def find_palindromes(index):
            #even
            left = index
            right = index + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                palindromes[left].append(s[left:right + 1])
                left -= 1
                right += 1
            #odd
            left = index - 1
            right = index + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                palindromes[left].append(s[left:right + 1])
                left -= 1
                right += 1

        def backtracking(pointer, path):
            if pointer >= len(s):
                result.append(path[:])
                return

            current_palindromes = palindromes[pointer]
            for palindrome in current_palindromes:
                path.append(palindrome)
                backtracking(pointer + len(palindrome), path)
                path.pop()

        result = []
        palindromes = [[letter] for letter in s]

        for i in range(len(s)):
            find_palindromes(i)

        backtracking(0, [])

        return result
def main():
    s = "aab"

    solution = Solution()

    result = solution.partition(s)
    
    print(result)


if __name__ == "__main__":
    main()