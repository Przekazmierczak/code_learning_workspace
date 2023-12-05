"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    def kthSmallest(self, root, k):
        count = [k]
        res = []
        def dfs(root, k):
            if not root:
                return
            
            if count[0] < 0:
                return
            
            dfs(root.left, k)

            count[0] -= 1
            if count[0] == 0:
                res.append(root.val)
                
            dfs(root.right, k)

        dfs(root, k)

        return res


def main():
    null = None
    root_list = [5,3,6,2,4,null,null,1]
    k = 3

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

    print(solution.kthSmallest(create_binary(root_list), k))


if __name__ == "__main__":
    main()