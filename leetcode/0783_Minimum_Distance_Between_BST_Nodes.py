"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1
Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    def minDiffInBST(self, root):
        stack = [(root, False)]
        res = float("inf")
        prev = float("-inf")
        
        while stack:
            node, visit = stack.pop()
            
            if visit:
                res = min(node.val - prev, res)
                prev = node.val
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
        
        return res


def main():
    root_list = [4,2,6,1,3]

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

    print(solution.minDiffInBST(create_binary(root_list)))


if __name__ == "__main__":
    main()