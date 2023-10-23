"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 
Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def swapPairs(self, head):
        result = current = ListNode()
        
        if head and not head.next:
            return head
        
        while head and head.next:
            current.next = head.next
            current = current.next
            
            head.next = head.next.next
            current.next = head
            
            head = head.next
            current = current.next
           
        return result.next

def main():
    head_list = [1,2,3,4]

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.swapPairs(head)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()