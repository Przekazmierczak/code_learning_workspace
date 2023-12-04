"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def diameterOfBinaryTree(self, root):
        def diameter(root):
            if not root:
                return (0, 0)

            left, result_left = diameter(root.left)
            right, result_right = diameter(root.right)

            result = left + right

            return (1 + max(left, right), max(result, result_left, result_right))
        return diameter(root)[1]




def main():
    null = None
    root_list = [1,2,3,4,5]

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

    print(solution.diameterOfBinaryTree(create_binary(root_list)))

if __name__ == "__main__":
    main()