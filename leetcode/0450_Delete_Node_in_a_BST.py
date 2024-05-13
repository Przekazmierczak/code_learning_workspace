"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    def deleteNode(self, root, key):
        def delete(node):
            if not node:
                return None
            elif node.val > key:
                node.left = delete(node.left)
            elif node.val < key:
                node.right = delete(node.right)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                node.right, val = getMin(node.right)
                node.val = val
                    
            return node
        
        def getMin(node):
            if not node.left:
                return node.right, node.val
            node.left, val = getMin(node.left)
            return node, val
            
        return delete(root)

def main():
    null = None
    root = [4,2,7,1,3,null,null,null,null,null,null]
    val = 5

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

    result = solution.deleteNode(create_binary(root), val)

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