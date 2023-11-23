"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        max_length = 0
            
        for num in nums:
            if (num - 1) not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                max_length = max(length, max_length)
        
        return max_length


def main():
    nums = [100,4,200,1,3,2]

    solution = Solution()

    result = solution.longestConsecutive(nums)
    
    print(result)


if __name__ == "__main__":
    main()