"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lowercase English letters.
"""

class Solution:
    # def removeDuplicates(self, s: str, k: int) -> str:
    def removeDuplicates(self, s, k):
        stack = []
        
        for l in s:
            if not stack or stack[-1][1] != l:
                stack.append([1, l])
            elif stack[-1][1] == l:
                stack[-1][0] += 1
            if stack[-1][0] == k:
                stack.pop()
        
        res = ""
        for element in stack:
            res += element[0] * element[1]
        return res
            

def main():
    s = "deeedbbcccbdaa"
    k = 3

    solution = Solution()

    result = solution.removeDuplicates(s, k)
    
    print(result)


if __name__ == "__main__":
    main()