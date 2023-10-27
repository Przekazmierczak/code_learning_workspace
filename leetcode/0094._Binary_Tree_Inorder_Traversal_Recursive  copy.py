"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def inorderTraversal(self, root):
        ans = []
        def list_append(node):
            if not node:
                return
            else:
                list_append(node.left)
                ans.append(node.val)
                list_append(node.right)
        list_append(root)
        return ans

def main():
    root = [1,None,2,3]

    solution = Solution()

    solution.inorderTraversal(root)
    
    print(solution)


if __name__ == "__main__":
    main()