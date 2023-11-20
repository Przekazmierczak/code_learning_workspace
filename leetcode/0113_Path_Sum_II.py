"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
"""
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def hasPathSum(self, root, targetSum):
        ans = []
        def PathSum(node, sum, current_nodes):
            if not node:
                return
            
            value = node.val
            current_nodes.append(value)
            sum -= value

            if not node.left and not node.right and sum == 0:
                ans.append(current_nodes[:])
                current_nodes.pop()
                return
            
            PathSum(node.left, sum, current_nodes)
            PathSum(node.right, sum, current_nodes)
            current_nodes.pop()
        
        PathSum(root, targetSum, [])

        return ans




def main():
    null = None
    root_list = [5,4,8,11,null,13,4,7,2,null,null,5,1]
    targetSum = 22

    def create_binary(root_list):
        root = TreeNode(root_list[0])
        node_list = [root]
        i = 1

        while i < len(root_list):
            node = node_list.pop(0)

            if root_list[i] != None:
                node.left = TreeNode(root_list[i])
                node_list.append(node.left)
            i += 1

            if i < len(root_list) and root_list[i] != None:
                node.right = TreeNode(root_list[i])
                node_list.append(node.right)
            i += 1

        return root

    solution = Solution()

    print(solution.hasPathSum(create_binary(root_list), targetSum))


if __name__ == "__main__":
    main()