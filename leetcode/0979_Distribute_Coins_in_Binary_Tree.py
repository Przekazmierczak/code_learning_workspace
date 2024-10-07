"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin.

Example 1:
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
"""

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def distributeCoins(self, root: Optional[TreeNode]) -> int:
    def distributeCoins(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            
            need_left, res_left = dfs(node.left)
            need_right, res_right = dfs(node.right)
            
            need = need_left + need_right + node.val - 1
            res = res_left + res_right + abs(need)
            
            return (need, res)
        
        need, res = dfs(root)
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
    root_list = [3,0,0]

    root = create_binary(root_list)

    solution = Solution()

    result = solution.distributeCoins(root)

    print(result)

if __name__ == "__main__":
    main()