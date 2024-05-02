"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    def isCompleteTree(self, root):
        que = deque([(root, 0,0)])
        prevRow = 0
        prevOrder = -1
        
        while que:
            node, row, order = que.popleft()
            
            if prevRow != row:
                if 2 ** prevRow != prevOrder + 1:
                    return False
                prevRow = row
                prevOrder = -1
            if order - prevOrder != 1:
                return False
            prevOrder = order
            
            if node.left:
                que.append((node.left, row +1, order * 2))
            if node.right:
                que.append((node.right, row +1, order * 2 + 1))
        
        return True


def main():
    root_list = [1,2,3,4,5,6]

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

    print(solution.isCompleteTree(create_binary(root_list)))

if __name__ == "__main__":
    main()