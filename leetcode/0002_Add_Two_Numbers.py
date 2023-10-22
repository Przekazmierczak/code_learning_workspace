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
        l1_string = ""
        while l1 != None:
            l1_string = str(l1.val) + l1_string
            l1 = l1.next
        l1_int = int(l1_string)
        
        l2_string = ""
        while l2 != None:
            l2_string = str(l2.val) + l2_string
            l2 = l2.next
        l2_int = int(l2_string)
        
        l3_int = l1_int + l2_int
        l3_string = str(l3_int)

        l3 = None
        while l3_string != "":
            value = int(l3_string[0])
            l3 = ListNode(val=value , next=l3)
            l3_string = l3_string[1:]

        return l3
            

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