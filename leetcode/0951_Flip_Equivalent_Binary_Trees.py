"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

Example 1:
Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def flipEquiv(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if (not root1 and root2) or (root1 and not root2) or root1.val != root2.val:
            return False
        
        if (not root1.left and not root2.left) or (root1.left and root2.left and root1.left.val == root2.left.val):
            left = self.flipEquiv(root1.left, root2.left)
            right = self.flipEquiv(root1.right, root2.right)
            return left and right
        elif (not root1.left and not root2.right) or (root1.left and root2.right and root1.left.val == root2.right.val):
            left = self.flipEquiv(root1.left, root2.right)
            right = self.flipEquiv(root1.right, root2.left)
            return left and right
        else:
            return False

def main():
    null = None
    root1 = [1,2,3,4,5,6,null,null,null,7,8]
    root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]

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

    print(solution.flipEquiv(create_binary(root1), create_binary(root2)))


if __name__ == "__main__":
    main()