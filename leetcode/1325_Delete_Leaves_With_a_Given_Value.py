"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

Constraints:

The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000
"""
from collections import deque

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    def removeLeafNodes(self, root, target):
        def dfs(node):
            if not node:
                return
            
            node.left = None if dfs(node.left) else node.left
            node.right = None if dfs(node.right) else node.right
            
            if not node.left and not node.right and node.val == target:
                return True
        
        return root if not dfs(root) else None
            
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

def main():
    null = None
    root_list = [1,2,3,2,null,2,4]
    target = 2

    root = create_binary(root_list)

    solution = Solution()

    result = solution.removeLeafNodes(root, target)

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