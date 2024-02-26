"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    def removeElements(self, head, val):
        dummy = ListNode()
        dummy.next = head
        
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

def main():
    head_list = [1,2,6,3,4,5,6]
    val = 6

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.removeElements(head, val)

    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)

if __name__ == "__main__":
    main()