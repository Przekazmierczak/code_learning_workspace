"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        ans = []
        top = [[] for _ in range(len(nums))]
        dic = {}
        
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        for key in dic:
            top[dic[key] - 1].append(key)
        
        for i in reversed(range(len(top))):
            if top[i]:
                ans.extend(top[i])
                if len(ans) == k: 
                    break
        return ans


def main():
    nums = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
    k = 3

    solution = Solution()

    result = solution.topKFrequent(nums, k)
    
    print(result)


if __name__ == "__main__":
    main()