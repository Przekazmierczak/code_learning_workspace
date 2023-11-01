"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def recoverTree(self, root: Optional[TreeNode]) -> None:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        current = root
        sus = []
        previous = TreeNode(float("-inf"))

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            node = stack.pop()

            if previous.val > node.val:
                sus.append((previous, node))

            previous = node
            current = node.right

        if len(sus) == 1:
            sus[0][0].val, sus[0][1].val = sus[0][1].val, sus[0][0].val
        else:
            sus[0][0].val, sus[1][1].val = sus[1][1].val, sus[0][0].val
        
        return root

def main():
    null = None
    root_list = [3,1,4,null,null,2]

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

    result = solution.recoverTree(create_binary(root_list))

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