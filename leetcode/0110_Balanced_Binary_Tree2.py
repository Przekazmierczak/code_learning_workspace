"""
Given a binary tree, determine if it is height-balanced.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def isBalanced(self, root):
        if_balance = [True]

        def check(root):
            if not root:
                return 0
            
            left = 1 + check(root.left)
            right = 1 + check(root.right)

            if abs(left - right) > 1:
                if_balance[0] = False
            
            return max(left , right)
        
        check(root)

        return if_balance[0]
        




def main():
    null = None
    root_list = [1,2,2,3,3,null,null,4,4]

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

    print(solution.isBalanced(create_binary(root_list)))


if __name__ == "__main__":
    main()