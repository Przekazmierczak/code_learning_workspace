"""
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
Return the length longest chain which can be formed.
You do not need to use up all the given intervals. You can select pairs in any order.

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].

Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 
Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
"""

class Solution:
    # def findLongestChain(self, pairs: List[List[int]]) -> int:
    def findLongestChain(self, pairs):
        pairs.sort()
        curr_max, res = float("-inf"), 0
        
        for i in range(len(pairs)):
            if pairs[i][0] > curr_max:
                res += 1
                curr_max = pairs[i][1]
            else:
                curr_max = min(curr_max, pairs[i][1])
        
        return res
            

def main():
    pairs = [[1,2],[7,8],[4,5]]

    solution = Solution()

    result = solution.findLongestChain(pairs)
    
    print(result)


if __name__ == "__main__":
    main()