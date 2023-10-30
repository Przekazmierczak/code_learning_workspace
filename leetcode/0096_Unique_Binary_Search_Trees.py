"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 
Constraints:

1 <= n <= 19
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def numTrees(self, n: int) -> int:
    def numTrees(self, n):
        if n <= 1:
            return 1
        
        memory = {}
        memory[0] = 1
        memory[1] = 1

        def count_trees(num_nodes):
            if num_nodes in memory:
                return memory[num_nodes]

            total_count = 0
            for root in range(1, num_nodes + 1):
                left_count = count_trees(root - 1)
                right_count = count_trees(num_nodes - root)
                total_count += left_count * right_count
            
            memory[num_nodes] = total_count

            return total_count

        return count_trees(n)



def main():
    n = 19

    solution = Solution()

    print(solution.numTrees(n))


if __name__ == "__main__":
    main()