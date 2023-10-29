"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def sortedArrayToBST(self, nums):
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        stack = [(root, nums[:mid], nums[mid + 1:])]

        while stack:
            node, left_list, right_list = stack.pop()

            if left_list:
                mid = len(left_list) // 2
                left_node = TreeNode(left_list[mid])
                node.left = left_node
                stack.append((left_node, left_list[:mid], left_list[mid + 1:]))
            
            if right_list:
                mid = len(right_list) // 2
                right_node = TreeNode(right_list[mid])
                node.right = right_node
                stack.append((right_node, right_list[:mid], right_list[mid + 1:]))
        
        return root


            
def main():
    nums = [-10,-3,0,5,9]

    solution = Solution()

    root = solution.sortedArrayToBST(nums)

    stack = [root]
    ans = []

    while stack:
        node = stack.pop(0)
        if node:
            ans.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        else:
            ans.append(None)
    
    print(ans)


if __name__ == "__main__":
    main()