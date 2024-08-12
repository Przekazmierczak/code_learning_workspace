"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
"""

class Solution:
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    def findErrorNums(self, nums):
        memo1 = {i for i in range(1, len(nums) + 1)}
        res = [None, None]
        
        for num in nums:
            if num in memo1:
                memo1.remove(num)
            else:
                res[0] = num

        res[1] = memo1.pop()
        
        return res
            

def main():
    nums = [1,2,2,4]

    solution = Solution()

    result = solution.findErrorNums(nums)
    
    print(result)


if __name__ == "__main__":
    main()