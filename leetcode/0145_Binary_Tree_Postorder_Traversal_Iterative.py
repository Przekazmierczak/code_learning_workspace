"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def postorderTraversal(self, root):
        stack = [(root, False)]
        res = []
        
        if not root:
            return res
        
        while stack:
            node, visit = stack.pop()
            if visit:
                res.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return res



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

    print(solution.postorderTraversal(create_binary(root_list)))


if __name__ == "__main__":
    main()