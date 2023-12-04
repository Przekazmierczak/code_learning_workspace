"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def lowestCommonAncestor(self, root, p, q):
        def lowCommAnc(root):
            if not root:
                return (False, False, "No result")
            
            left_if_p, left_if_q, left_result = lowCommAnc(root.left)
            right_if_p, right_if_q, right_result = lowCommAnc(root.right)

            if_p = left_if_p or right_if_p
            if_q = left_if_q or right_if_q

            if root.val == p:
                if_p = True
            if root.val == q:
                if_q = True

            if left_result != "No result":
                result = left_result
            elif right_result != "No result":
                result = right_result
            else:
                result = "No result"

            if if_p and if_q and result == "No result":
                result = root.val
            
            return (if_p, if_q, result)
        
        return lowCommAnc(root)[2]



def main():
    null = None
    root_list = [6,2,8,0,4,7,9,null,null,3,5]
    p = 2
    q = 4

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

    print(solution.lowestCommonAncestor(create_binary(root_list), p, q))

if __name__ == "__main__":
    main()