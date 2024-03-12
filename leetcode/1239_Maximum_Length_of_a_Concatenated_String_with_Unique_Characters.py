"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""

class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    def maxLength(self, arr):
        unique = set()
        
        def backtrack(i, l):
            res = 0
            if i >= len(arr):
                return l
            
            possible = True
            for j in range(len(arr[i])):
                if arr[i][j] in unique:
                    possible = False
                    j -= 1
                    break
                unique.add(arr[i][j])
                
            if possible:
                res = max(backtrack(i + 1, l + len(arr[i])), res)
            
            for k in range(j + 1):
                unique.remove(arr[i][k])
                    
            res = max(backtrack(i + 1, l), res)
            
            return res
        
        return backtrack(0, 0)
            

def main():
    arr = [17,18,5,4,6,1]

    solution = Solution()

    result = solution.maxLength(arr)
    
    print(result)


if __name__ == "__main__":
    main()