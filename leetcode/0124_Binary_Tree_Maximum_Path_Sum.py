"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    def maxPathSum(self, root):
        def maxSum(node):
            if not node:
                return (float("-inf"), float("-inf"))
            
            max_left, result_left = maxSum(node.left)
            max_right, result_right = maxSum(node.right)

            max_path = max(max_left + node.val, max_right + node.val, node.val)
            result = max(max_left + max_right + node.val, result_left, result_right, max_path)

            return(max_path, result)
    
        return maxSum(root)[1]



def main():
    null = None
    root_list = [-10,9,20,null,null,15,7]

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

    print(solution.maxPathSum(create_binary(root_list)))


if __name__ == "__main__":
    main()