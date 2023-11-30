"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None:
    def reorderList(self, head):
        # find middle
        fast, slow = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # reverse
        prev = None

        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt
        
        # join
        head2 = prev
        dummy = ListNode(0)
        current = dummy

        while head:
            current.next = head
            current = current.next
            head = head.next

            if head2:
                current.next = head2
                current = current.next
                head2 = head2.next

        return dummy.next

def main():
    head_list = [1,2,3,4,5]

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.reorderList(head)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()