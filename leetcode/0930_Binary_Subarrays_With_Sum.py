"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""

class Solution:
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    def numSubarraysWithSum(self, nums, goal):
        def find(x):
            l, r = 0, 0
            curr = 0
            res = 0
            
            for r in range(len(nums)):
                curr += nums[r]
                while curr > x:
                    curr -= nums[l]
                    l += 1
                res += r - l + 1
            return res
        
        return find(goal) - find(goal - 1) if goal > 0 else find(goal)
            

def main():
    nums = [1,0,1,0,1]
    goal = 2

    solution = Solution()

    result = solution.numSubarraysWithSum(nums, goal)
    
    print(result)


if __name__ == "__main__":
    main()