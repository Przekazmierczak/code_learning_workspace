"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.
Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
"""

class Solution:
    # def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    def maxSumAfterPartitioning(self, arr, k):
        LEN = len(arr)
        memo = {}
        
        def dfs(i, rest, curr_max):
            if i == LEN:
                return 0
            if (i, rest) in memo:
                return memo[(i, rest)]
            curr_max = max(curr_max, arr[i])
            if rest < k:
                res = max(dfs(i + 1, rest + 1, curr_max), curr_max * rest + dfs(i + 1, 1, 0))
            else:
                res = curr_max * rest + dfs(i + 1, 1, 0)
            memo[(i, rest)] = res
            return res
            
        return dfs(0, 1, 0)
            

def main():
    arr = [1,4,1,5,7,3,6,1,9,9,3]
    k = 4

    solution = Solution()

    result = solution.maxSumAfterPartitioning(arr, k)
    
    print(result)


if __name__ == "__main__":
    main()