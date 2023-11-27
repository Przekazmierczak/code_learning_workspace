"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from collections import deque
class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    def maxSlidingWindow(self, nums, k):
        que = deque([])
        ans = []
        
        left = 0
        
        for right in range(len(nums)):
            while que and nums[que[-1]] < nums[right]:
                que.pop()
                
            que.append(right)
            ans.append(nums[que[0]])
            
            if right + 1 >= k:
                if left == que[0]:
                    que.popleft()
                left += 1
            
        return ans[k - 1:]


def main():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    solution = Solution()

    result = solution.maxSlidingWindow(nums, k)
    
    print(result)


if __name__ == "__main__":
    main()