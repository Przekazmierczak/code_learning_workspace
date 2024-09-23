"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def leafSimilar(self, root1, root2):
        stack1 = [root1]
        stack2 = [root2]
        
        while stack1 and stack2:
            node1 = stack1.pop()
            while node1.left or node1.right:
                if node1.left:
                    stack1.append(node1.left)
                if node1.right:
                    stack1.append(node1.right)
                node1 = stack1.pop()
            
            node2 = stack2.pop()
            while node2.left or node2.right:
                if node2.left:
                    stack2.append(node2.left)
                if node2.right:
                    stack2.append(node2.right)
                node2 = stack2.pop()
                
            if node1.val != node2.val:
                return False
        
        return True if not stack1 and not stack2 else False

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
    root1_list = [3,5,1,6,2,9,8,null,null,7,4]
    root2_list = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    root1 = create_binary(root1_list)
    root2 = create_binary(root2_list)


    solution = Solution()

    print(solution.leafSimilar(root1, root2))


if __name__ == "__main__":
    main()