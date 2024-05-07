"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:

Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 
Constraints:

1 <= n <= 20
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    def allPossibleFBT(self, n):
        memo = {}
        def FBT(n):
            if n in memo:
                return memo[n]
            
            if n == 0:
                return [TreeNode()]
            
            nodes = []
            
            for i in range(1, n):
                left = FBT(i - 1)
                right = FBT(n - i - 1)
                for left_node in left:
                    for right_node in right:
                        new_node = TreeNode()
                        new_node.left = left_node
                        new_node.right = right_node
                    
                        nodes.append(new_node)
                        
            memo[n] = nodes
            return nodes
        
        res = []
        roots = FBT(n - 1)
        for root in roots:
            res.append(root)
        
        return res

def main():
    n = 7

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

    result = solution.allPossibleFBT(n)

    answer = []

    for res in result:
        stack = deque([(res, 0)])
        ans = []
        
        while stack:
            node, level = stack.popleft()
            
            if node:           
                ans.append(node.val)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
            else:
                ans.append(None)
        
        while ans[-1] == None:
            if ans[-1] == None:
                ans.pop()

        answer.append(ans)
        
    print(answer)


if __name__ == "__main__":
    main()