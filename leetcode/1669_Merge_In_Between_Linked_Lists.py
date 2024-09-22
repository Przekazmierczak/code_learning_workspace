"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure indicate the result:

Build the result list and return its head.

Example 1:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:  
    def mergeInBetween(self, list1, a, b, list2):  
        nodeb = list1
        for i in range(b + 1):
            if i == a - 1:
                nodea = nodeb
            nodeb = nodeb.next
            
        node2 = list2
        while node2.next:
            node2 = node2.next
        
        nodea.next = list2
        node2.next = nodeb
        
        return list1
            
def create_link_list(list_):
    head = None
    for i in reversed(range(len(list_))):
        head = ListNode(list_[i], head)

    return head

def main():
    list1 = [10,1,13,6,9,5]
    list2 = [1000000,1000001,1000002]
    a = 3
    b = 4

    head1 = create_link_list(list1)
    head2 = create_link_list(list2)

    solution = Solution()

    result = solution.mergeInBetween(head1, a, b, head2)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)

if __name__ == "__main__":
    main()