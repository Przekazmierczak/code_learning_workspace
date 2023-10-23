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
        current = result = ListNode(0)
        
        while True:
            biggest = None
            for index, node_list in enumerate(lists):
                if node_list != None:
                    if biggest == None or biggest.val > node_list.val:
                        biggest = node_list
                        biggest_index = index
                        
            if biggest == None:
                return result.next
       
            current.next = biggest
            current = current.next
            
            lists[biggest_index] = lists[biggest_index].next  

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