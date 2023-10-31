"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 
Constraints:

1 <= n <= 8
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    def generateTrees(self, n):
        def generate(left, right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            
            ans = []
            
            for root in range(left, right + 1):           
                left_nodes = generate(left, root - 1)
                right_nodes = generate(root + 1, right)
                
                for left_node in left_nodes:
                    for right_node in right_nodes:                   
                        root_node = TreeNode(root, left_node, right_node)
                        ans.append(root_node)
            return ans
        return generate(1, n)



def main():
    n = 3

    solution = Solution()

    trees = solution.generateTrees(n)
    
    result = []

    for tree in trees:
        stack = deque([(tree, 0)])
        ans = []
        
        while stack:
            node, level = stack.popleft()
            
            if node:
                if len(ans) <= level:
                    ans.append([])
                
                ans[level].append(node.val)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
                
        result.append(ans)
            
    print(result)

if __name__ == "__main__":
    main()