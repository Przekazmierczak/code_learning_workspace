"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        r = prev.next
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(r)

        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
                curr = curr.next
            else:
                curr.next = right
                right = right.next
                curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next
            

def main():
    head_list = [4,2,1,3]

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.sortList(head)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()