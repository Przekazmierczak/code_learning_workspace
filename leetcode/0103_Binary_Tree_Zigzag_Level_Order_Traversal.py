"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    def zigzagLevelOrder(self, root):
        level = 0
        ans = []
        stack= deque([(root, level)])
       
        while stack:
            node, level = stack.popleft()
            
            if node:
                if len(ans) <= level:
                    ans.append(deque([]))
                if level % 2 == 0:
                    ans[level].append(node.val)
                else:
                    ans[level].appendleft(node.val)
                
                stack.append((node.left, level +1))
                stack.append((node.right, level +1))
                
        return ans



def main():
    null = None
    root_list = [3,9,20,null,null,15,7]

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

    print(solution.zigzagLevelOrder(create_binary(root_list)))


if __name__ == "__main__":
    main()