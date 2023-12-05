"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    def rightSideView(self, root):
        if not root:
            return []
        
        stack = deque([root])
        ans = []
        
        while stack:
            if_first = True
            for i in range(len(stack)):
                node = stack.popleft()
                
                if if_first:
                    ans.append(node.val)
                    if_first = False

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return ans
        
        


def main():
    null = None
    root = [3,4,5,1,2,null,null,null,null,0]
    subRoot = [4,1,2]

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

    print(solution.rightSideView(create_binary(root)))


if __name__ == "__main__":
    main()