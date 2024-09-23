"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 104
-1 <= leftChild[i], rightChild[i] <= n - 1
"""

class Solution:
    # def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        def check(root):
            visit = [False] * n
            stack = [root]
            
            while stack:
                node = stack.pop()
                if visit[node]:
                    return False
                visit[node] = True
                
                if leftChild[node] != -1:
                    stack.append(leftChild[node])
                if rightChild[node] != -1:
                    stack.append(rightChild[node])
            
            for node in visit:
                if not node:
                    return False
            return True
        
        roots = [True] * n
        
        for i in range(n):
            if leftChild[i] != -1:
                roots[leftChild[i]] = False
            if rightChild[i] != -1:
                roots[rightChild[i]] = False
        
        for root in range(n):
            if roots[root]:
                return check(root)
        return False
            

def main():
    n = 4
    leftChild = [1,-1,3,-1]
    rightChild = [2,-1,-1,-1]

    solution = Solution()

    result = solution.validateBinaryTreeNodes(n, leftChild, rightChild)
    
    print(result)


if __name__ == "__main__":
    main()