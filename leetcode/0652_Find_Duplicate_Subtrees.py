"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:

Input: root = [2,1,1]
Output: [[1]]
Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 
Constraints:

The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    def findDuplicateSubtrees(self, root):
        hashMap = {}
        ans = []
        def makeDic(node):
            if not node:
                return [None]
            
            left = makeDic(node.left)
            right = makeDic(node.right)
            res = left + right + [node.val]
            if tuple(res) not in hashMap:
                hashMap[tuple(res)] = [node, False]
            else:
                if not hashMap[tuple(res)][1]:
                    ans.append(node)
                    hashMap[tuple(res)][1] = True
                    
            return res
        
        makeDic(root)
        
        return ans
            

def main():
    null = None
    root_list = [1,2,3,4,null,2,4,null,null,4]

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

    print(solution.findDuplicateSubtrees(create_binary(root_list)))


if __name__ == "__main__":
    main()