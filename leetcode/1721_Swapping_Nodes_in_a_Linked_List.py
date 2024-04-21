"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def swapNodes(self, head, k):
        slow, fast = head, head
        
        for _ in range(k - 1):
            fast = fast.next
            
        swap = fast
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        swap.val, slow.val = slow.val, swap.val
        
        return head


def main():
    head_list = [7,9,6,6,7,8,3,0,9,5]
    k = 5

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.swapNodes(head, k)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()