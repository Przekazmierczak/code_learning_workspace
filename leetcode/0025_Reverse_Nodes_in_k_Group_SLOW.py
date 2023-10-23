"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head

        result = current = ListNode()

        def rotate(head, current, k):
            head_check = head
            for _ in range(k):
                if head_check == None:
                    return True
                head_check = head_check.next
                
            current_result = current
            for i in reversed(range(1, k)):
                for _ in range(i):
                    current.next = head.next
                    current = current.next
                    
                    head.next = head.next.next
                    current.next = head

                    head = current
                    head = head.next

                current = current_result
                head = current_result.next


        while True:
            check = rotate(head, current, k)

            if check == True:
                return result.next
            
            head = current.next
            for _ in range(k):
                current = current.next
                head = head.next



def main():
    head_list = [1,2,3,4,5,6,7,8,9]
    k = 3

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.reverseKGroup(head, k)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()