"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 
Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def mergeKLists(self, lists):
        def merge_lists(lists):
            if not lists:
                return None

            if len(lists) == 1:
                return lists[0]
            
            half = len(lists) // 2
            left = lists[:half]
            right = lists[half:]

            left = merge_lists(left)
            right = merge_lists(right)

            return merge(left, right)

        def merge(left, right):
            current = result = ListNode(0)

            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next

            if not left:
                current.next = right
            elif not right:
                current.next = left
            
            return result.next
        
        return merge_lists(lists)



def main():
    head_list = [[1,4,5],[1,3,4],[2,6]]
    lists = []
    for element in head_list:
        head = None
        for i in reversed(range(len(element))):
            head = ListNode(element[i], head)
        lists.append(head)

    solution = Solution()

    result = solution.mergeKLists(lists)
    
    result_node_list = []
    while result:
        result_node_list.append(result.val)
        result = result.next

    print(result_node_list)



if __name__ == "__main__":
    main()