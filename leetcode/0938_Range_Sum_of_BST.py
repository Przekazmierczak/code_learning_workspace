"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return 0
            
            res = 0
            if low <= node.val <= high:
                res = node.val
            
            if node.val > low:
                res += dfs(node.left)
            
            if node.val < high:
                res += dfs(node.right)
            
            return res
        
        return dfs(root)

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
    root_list = [10,5,15,3,7,null,18]
    root = create_binary(root_list)
    low = 7
    high = 15

    solution = Solution()

    print(solution.rangeSumBST(root, low, high))


if __name__ == "__main__":
    main()