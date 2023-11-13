"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def rotateRight(self, head, k):
        if not head:
            return head
        current = head
        length = 0
        
        while current:
            current = current.next
            length += 1
            
        k %= length
        
        if k == 0:
            return head
        
        fast = head
        
        for _ in range(length - k - 1):
            fast = fast.next
        
        slow = fast
        fast = fast.next
        slow.next = None
        
        end = fast
        while end.next:
            end = end.next
            
        end.next = head
        
        return fast

def main():
    head_list = [1,2,3,4,5]
    k = 2

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.rotateRight(head, k)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()