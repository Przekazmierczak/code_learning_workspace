"""
You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 
Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""

class Solution:
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    def findMaxForm(self, strs, m, n):
        LEN = len(strs)
        for i in range(LEN):
            nums = [0, 0]
            for num in strs[i]:
                if num == "0":
                    nums[0] += 1
                else:
                    nums[1] += 1
            strs[i] = nums
        
        memo = {}
        
        def dfs(i, zeroes, ones):
            if (i, zeroes, ones) in memo:
                return memo[(i, zeroes, ones)]
            if i == LEN:
                return 0
            
            res = dfs(i + 1, zeroes, ones)
            nxt_zeroes = zeroes + strs[i][0]
            nxt_ones = ones + strs[i][1]
            if nxt_zeroes <= m and nxt_ones <= n:
                res = max(dfs(i + 1, zeroes + strs[i][0], ones + strs[i][1]) + 1, res)
            memo[(i, zeroes, ones)] = res
            return res
        
        return dfs(0, 0, 0)
            

def main():
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3

    solution = Solution()

    result = solution.findMaxForm(strs, m, n)
    
    print(result)


if __name__ == "__main__":
    main()