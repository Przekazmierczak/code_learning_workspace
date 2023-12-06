"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = deque([root])
        seria = ""
        
        while stack:
            node = stack.popleft()
            if node:
                seria += str(node.val) + ","
                stack.append(node.left)
                stack.append(node.right)
            else:
                seria += "#,"
        return seria
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        value = ""
        state = "root"
        stack = deque([])
        i = 0
        while i < len(data):
            while data[i] != ",":
                value += data[i]
                i += 1
                
            if state == "root":
                if value != "#":
                    root = TreeNode(int(value))
                    stack.append(root)
                else:
                    root = None
                state = "left"
                
            elif state == "left":
                node = stack.popleft()
                if value != "#":
                    node.left = TreeNode(int(value))
                    stack.append(node.left)
                state = "right"
            
            else:
                if value != "#":
                    node.right = TreeNode(int(value))
                    stack.append(node.right)
                state = "left"
            
            value = ""
            i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))