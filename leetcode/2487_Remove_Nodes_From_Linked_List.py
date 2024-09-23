"""
You are given the head of a linked list.
Remove every node which has a node with a greater value anywhere to the right side of it.
Return the head of the modified linked list.

Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def removeNodes(self, head):
        stack = []
        curr = head
        curr_max = None
        
        while curr:
            stack.append(curr)
            curr = curr.next
        
        while stack:
            curr = stack.pop()
            if curr_max:
                if curr_max.val <= curr.val:
                    curr.next = curr_max
                    curr_max = curr
                
            else:
                curr_max = curr
        
        return curr_max
            
def create_link_list(list_):
    head = None
    for i in reversed(range(len(list_))):
        head = ListNode(list_[i], head)

    return head

def main():
    list1 = [5,2,13,3,8]

    head = create_link_list(list1)

    solution = Solution()

    result = solution.removeNodes(head)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)

if __name__ == "__main__":
    main()