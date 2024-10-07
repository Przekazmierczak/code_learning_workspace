"""
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
As a reminder, any shorter prefix of a string is lexicographically smaller.
For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example 1:
Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"
 
Constraints:

The number of nodes in the tree is in the range [1, 8500].
0 <= Node.val <= 25
"""

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    def smallestFromLeaf(self, root):
        def check(res, array):
            for i in range(1, len(res) + 1):
                if array[-i] < res[-i] or (array[-i] == res[-i] and i == len(array)):
                    return True
                elif array[-i] > res[-i]:
                    return False
            return False
        
        def dfs(node):
            nonlocal res
            if not node:
                return
            
            curr.append(node.val)
            if not node.left and not node.right and (not res or check(res, curr)):
                res = curr.copy()
            dfs(node.left)
            dfs(node.right)
            curr.pop()
        
        curr = []
        res = []
        
        dfs(root)
        
        letters = []
        for i in range(len(res) - 1, -1, -1):
            letters.append(chr(res[i] + ord("a")))
        
        return "".join(letters)
            
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
    root_list = [0,1,2,3,4,3,4]

    root = create_binary(root_list)

    solution = Solution()

    result = solution.smallestFromLeaf(root)

    print(result)

if __name__ == "__main__":
    main()