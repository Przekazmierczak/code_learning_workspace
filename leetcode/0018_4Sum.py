"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

class Solution:
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def fourSum(self, nums, target):
        ans = set()

        sorted_nums = sorted(nums)
        length = len(sorted_nums)

        first_index = 0

        while first_index < length - 3:
            second_index = first_index + 1
           
            while second_index < length - 2:
                left = second_index + 1
                right = length - 1
                
                while left < right:
                    sum = sorted_nums[first_index] + sorted_nums[second_index] + sorted_nums[left] + sorted_nums[right]

                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        result = (sorted_nums[first_index], sorted_nums[second_index], sorted_nums[left], sorted_nums[right])
                        ans.add(result)
                        
                        left += 1
                        right -= 1

                second_index += 1
            first_index += 1
       
        return ans



def main():
    nums = [-3,-2,-1,0,0,1,2,3]
    # [-2,-1,0,0,1,2]
    target = 0

    solution = Solution()

    result = solution.fourSum(nums, target)
    
    print(result)


if __name__ == "__main__":
    main()