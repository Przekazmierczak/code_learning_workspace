"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def flatten(self, root: Optional[TreeNode]) -> None:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        current = root

        while current:
            if current.left:

                temp = current.left
                while temp.right:
                    temp = temp.right
                
                temp.right = current.right
                current.right = current.left
                current.left = None

            current = current.right
                
        return root



def main():
    null = None
    root_list = [1,2,5,3,4,7,6]

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

    result = solution.flatten(create_binary(root_list))

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