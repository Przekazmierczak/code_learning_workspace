"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        node = head
        result = ListNode()
        current_result = result
        value = node.val

        while node:
            if node.next and node.next.val == value:
                while node.next and node.next.val == value:
                    node = node.next
                if not node.next:
                    break

            else:
                current_result.next = node
                current_result = current_result.next
                
            if not node.next:
                current_result.next = node
                current_result = current_result.next
                break
            node = node.next
            value = node.val

        current_result.next = None
        return result.next


def main():
    head_list = [1,2,3,3,4,4,5]

    head = None
    for i in reversed(range(len(head_list))):
        head = ListNode(head_list[i], head)

    solution = Solution()

    result = solution.deleteDuplicates(head)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()