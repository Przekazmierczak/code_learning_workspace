"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def removeNthFromEnd(self, head, n):
        front = head
        back = head
        
        for _ in range(n + 1):
            # when the first element of the list need to be thrown
            if not front:
                return head.next
            front = front.next
        
        while front:
            front = front.next
            back = back.next
            
        back.next = back.next.next
        
        return head


def main():
    head_list = [1,2,3,4,5]
    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)
   
    n = 2
    
    solution = Solution()

    result = solution.removeNthFromEnd(head, n)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()