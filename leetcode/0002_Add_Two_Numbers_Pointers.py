"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1, l2):
        remainer = 0
        new_list = ListNode(0)
        result = new_list
        while l1 or l2 or remainer:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum_ = val1 + val2 + remainer
            new_list.next = ListNode(sum_ % 10)
            remainer = sum_ // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            new_list = new_list.next
        
        return result.next


def main():

    l1_list = [2,4,3]
    l2_list = [5,6,4]

    l1 = None
    for i in reversed(range(len(l1_list))):
        l1 = ListNode(l1_list[i], l1)

    l2 = None
    for i in reversed(range(len(l2_list))):
        l2 = ListNode(l2_list[i], l2)

    solution = Solution()

    result = solution.addTwoNumbers(l1, l2)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)

if __name__ == "__main__":
    main()