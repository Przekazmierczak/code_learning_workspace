"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:

The number of nodes in the tree will be in the range [0, 104].
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
    # def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    def largestValues(self, root):
        if not root:
            return []
        
        que = deque([(root, 0)])
        lvl, curr = 0, float("-inf")
        res = []
        
        while que:
            node, clvl = que.popleft()
            if clvl != lvl:
                res.append(curr)
                lvl = clvl
                curr = float("-inf")
            curr = max(curr, node.val)
            
            if node.left:
                que.append((node.left, clvl + 1))
            if node.right:
                que.append((node.right, clvl + 1))
        
        res.append(curr)
        return res

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
    root_list = [1,3,2,5,3,null,9]
    root = create_binary(root_list)

    solution = Solution()

    print(solution.largestValues(root))


if __name__ == "__main__":
    main()