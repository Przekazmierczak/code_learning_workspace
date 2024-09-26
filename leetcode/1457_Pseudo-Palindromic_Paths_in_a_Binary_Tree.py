"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 9
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    def pseudoPalindromicPaths(self, root):
        def checkPali(vals):
            middle = False
            for val in vals:
                if vals[val] % 2:
                    if not middle:
                        middle = True
                    else:
                        return False
            return True
        
        def dfs(node):
            if not node:
                return 0
            
            if node.val not in dic:
                dic[node.val] = 0
            dic[node.val] += 1
                
            res = 0
            if not node.left and not node.right and checkPali(dic):
                res = 1
                
            res += dfs(node.left) + dfs(node.right)
            dic[node.val] -= 1
            
            return res
            
        dic = {}
        
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
    root_list = [2,1,1,1,3,null,null,null,null,null,1]
    root = create_binary(root_list)

    solution = Solution()

    print(solution.pseudoPalindromicPaths(root))


if __name__ == "__main__":
    main()