"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution:
    # def majorityElement(self, nums: List[int]) -> List[int]:
    def majorityElement(self, nums):
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            
            if len(dic) > 2:
                toRemove = []
                for element in dic:
                    dic[element] -= 1
                    if dic[element] == 0:
                        toRemove.append(element)
                for remove in toRemove:
                    dic.pop(remove)
        
        res = []    
        for num in dic:
            if nums.count(num) > len(nums) / 3:
                res.append(num)
        
        return res
            

def main():
    nums = [3,2,3]

    solution = Solution()

    result = solution.majorityElement(nums)
    
    print(result)


if __name__ == "__main__":
    main()