"""
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).

Constraints:

The number of nodes in the tree is in the range [1, 3000].
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
    # def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def widthOfBinaryTree(self, root):
        que = deque([(root, 0,0)])
        prevRow = -1
        res = 0
        left = 0
        right = 0
        
        while que:
            node, row, order = que.popleft()
            if prevRow != row:
                res = max(res, right - left + 1)
                left = order
                prevRow = row
            right = order
            if node.left:
                que.append((node.left, row +1, order * 2))
            if node.right:
                que.append((node.right, row +1, order * 2 + 1))
        
        res = max(res, right - left + 1)
        return res

def main():
    null = None
    root_list = [1,3,2,5,null,null,9,6,null,7]

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

    print(solution.widthOfBinaryTree(create_binary(root_list)))


if __name__ == "__main__":
    main()