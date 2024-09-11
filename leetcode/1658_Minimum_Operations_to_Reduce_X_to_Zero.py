"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""

class Solution:
    # def minOperations(self, nums: List[int], x: int) -> int:
    def minOperations(self, nums, x):
        summ = sum(nums)
        goal = summ - x
        curr, l, r = 0, 0, 0
        res = float("inf")
        
        if goal < 0:
            return -1
        
        while True:
            if curr == goal:
                res = min(res, len(nums) - (r - l))
            if curr <= goal and r < len(nums):
                curr += nums[r]
                r += 1
            else:
                if curr <= goal:
                    break
                curr -= nums[l]
                l += 1
        
        if res == float("inf"):
            res = -1
        return res
            

def main():
    nums = [5,6,7,8,9]
    x = 4

    solution = Solution()

    result = solution.minOperations(nums, x)
    
    print(result)


if __name__ == "__main__":
    main()