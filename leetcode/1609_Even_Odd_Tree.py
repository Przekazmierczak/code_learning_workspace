"""
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

Example 2:
Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:
Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 106
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
    def isEvenOddTree(self, root):
        que = deque([(root, 0)])
        currLvl = -1
        
        while que:
            node, lvl = que.popleft()
            if currLvl != lvl:
                if lvl % 2:
                    prev = float("inf")
                else:
                    prev = float("-inf")
                currLvl = lvl
                
            if lvl % 2:
                if prev <= node.val or node.val % 2:
                    return False
                else:
                    prev = node.val
            else:
                if prev >= node.val or not node.val % 2:
                    return False
                else:
                    prev = node.val
            if node.left:
                que.append((node.left, lvl + 1))
            if node.right:
                que.append((node.right, lvl + 1))
                
        return True

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
    root_list = [1,10,4,3,null,7,9,12,8,6,null,null,2]
    root = create_binary(root_list)

    solution = Solution()

    print(solution.isEvenOddTree(root))


if __name__ == "__main__":
    main()