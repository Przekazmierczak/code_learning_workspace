"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    def mergeTrees(self, root1, root2):
        if not root1 and not root2:
            return None
            
        root = TreeNode()
        root.val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
            
        return root

def main():
    null = None
    root1 = [1,3,2,5]
    root2 = [2,1,3,null,4,null,7]

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
    result = solution.mergeTrees(create_binary(root1), create_binary(root2))

    stack = deque([(result, 0)])
    ans = []
    
    while stack:
        node, level = stack.popleft()
        
        if node:           
            ans.append(node.val)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
        else:
            ans.append(None)
    
    while ans[-1] == None:
        if ans[-1] == None:
            ans.pop()

    print(ans)



if __name__ == "__main__":
    main()