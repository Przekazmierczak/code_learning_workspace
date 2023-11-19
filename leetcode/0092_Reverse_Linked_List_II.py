"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 
Follow up: Could you do it in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    def reverseBetween(self, head, left, right):
        before_sublist = ListNode()
        reversed_sublist = ListNode()
        before_sublist.next = head
        current = before_sublist

        for _ in range(left - 1):
             current = current.next

        sublist_last = current.next

        for _ in range(right - left + 1):
            reversed_sublist.next, reversed_sublist.next.next, current.next = current.next, reversed_sublist.next, current.next.next

        current.next, sublist_last.next = reversed_sublist.next, current.next

        return before_sublist.next
                 
                 

def main():

    head_list = [1,2,3,4,5]
    left = 2
    right = 4

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.reverseBetween(head, left, right)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)

if __name__ == "__main__":
    main()