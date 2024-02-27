"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:

1 <= n <= 231 - 1
"""

class Solution:
    # def arrangeCoins(self, n: int) -> int:
    def arrangeCoins(self, n):
        l, r = 1, n
        
        while l <= r:
            mid = (l + r) // 2
            curr_sum = (mid/2)*(mid +1)
            
            if curr_sum > n:
                r = mid - 1
            elif curr_sum < n:
                l = mid + 1
            else:
                return mid
            
        return r
            

def main():
    n = 5

    solution = Solution()

    result = solution.arrangeCoins(n)
    
    print(result)


if __name__ == "__main__":
    main()