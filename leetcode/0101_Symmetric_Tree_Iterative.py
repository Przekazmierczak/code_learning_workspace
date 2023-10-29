"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false
 
Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 
Follow up: Could you solve it both recursively and iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def isSymmetric(self, root):
        stack = [root.left, root.right]

        while stack:
            left = stack.pop()
            right = stack.pop()
            if left == None and right == None:
                continue
            
            elif left == None or right == None:
                return False
            
            elif left.val == right.val:
                stack.append(left.left)
                stack.append(right.right)
                stack.append(left.right)
                stack.append(right.left)
            
            else:
                return False
            
        return True


def main():
    root_list = [1,2,2,None,3,None,3]

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

    print(solution.isSymmetric(create_binary(root_list)))


if __name__ == "__main__":
    main()