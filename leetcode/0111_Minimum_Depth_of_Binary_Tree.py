"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 
Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    def minDepth(self, root):
        if not root:
            return 0
        
        depth = 1
        stack = deque([(root, depth)])

        while stack:
            node, depth = deque.popleft(stack)
            if node:
                if not node.left and not node.right:
                    break
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return depth


def main():
    null = None
    root_list = [3,9,20,null,null,15,7]

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

    print(solution.minDepth(create_binary(root_list)))


if __name__ == "__main__":
    main()