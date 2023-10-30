"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:

Input: root = [2,1,3]
Output: true
Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def isValidBST(self, root):
        def check(root):
            if not root:
                return float('-inf'), float('inf'), True
            
            left_max, left_min, left_status = check(root.left)
            right_max, right_min, right_status = check(root.right)

            if left_status and right_status and left_max >= root.val >= right_min:
                status = True
            else:
                status = False
                
            current_max = max(left_max, right_max, root.val)
            current_min = min(left_min, right_min, root.val)

            return current_max, current_min, status

        return check(root)[2]



def main():
    null = None
    root_list = [5,1,4,null,null,3,6]

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

    print(solution.isValidBST(create_binary(root_list)))


if __name__ == "__main__":
    main()