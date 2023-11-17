"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 
Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    def partition(self, head, x):
        dummy = ListNode()
        dummy.next = head
        fast, slow = dummy, dummy
        
        while fast.next and fast.next.val < x:
            fast, slow = fast.next, slow.next

        while fast.next:
            if fast.next.val < x:
                slow.next, slow.next.next, fast.next = fast.next, slow.next, fast.next.next
                slow = slow.next
            else:
                fast = fast.next
        return dummy.next


def main():
    head_list = [1,4,3,2,5,2]
    x = 3

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.partition(head, x)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()