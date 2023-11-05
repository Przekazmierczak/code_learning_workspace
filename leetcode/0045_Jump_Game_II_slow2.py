"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 
Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

class Solution:
    # def jump(self, nums: List[int]) -> int:
    def jump(self, nums):
        def jump_track(nums, index):
            if index >= len(nums) - 1:
                return 0
            
            min_jumps = float("inf")
            
            for i in range(1, nums[index] + 1):
                jumps =  jump_track(nums, index + i) + 1
                min_jumps = min(min_jumps, jumps)

            return min_jumps
    
        return jump_track(nums, 0)


def main():
    nums = [2,3,0,1,4,6]

    solution = Solution()

    result = solution.jump(nums)
    
    print(result)


if __name__ == "__main__":
    main()