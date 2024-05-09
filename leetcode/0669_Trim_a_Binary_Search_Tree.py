"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Example 1:

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]
Example 2:

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree.
0 <= low <= high <= 104
"""
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    def trimBST(self, root, low, high):
        def trim(node, prev, direct):
            if direct == "l":
                prev.left = node
            else:
                prev.right = node
                
        dummy = TreeNode(low, None, root)
        stack = [(root, dummy, "r")]
        
        while stack:
            node, prev, direct = stack.pop()
            if not node:
                trim(None, prev, direct)
                    
            elif node.val < low:
                stack.append((node.right, prev, direct))
                
            elif node.val > high:
                stack.append((node.left, prev, direct))
                
            else:
                trim(node, prev, direct)  
                stack.append((node.left, node, "l"))
                stack.append((node.right, node, "r"))
        return dummy.right



def main():
    null = None
    root = [3,0,4,null,2,null,null,1]
    low = 1
    high = 3

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

    result = solution.trimBST(create_binary(root), low, high)

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