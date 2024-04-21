"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        
        for _ in range(index):
            curr = curr.next
            if not curr:
                break
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            newNode = Node(val)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(val)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        newNode = Node(val)
        
        for _ in range(index):
            if curr:
                curr = curr.next
            else:
                return
        if index == 0:
            self.addAtHead(val)
        elif not curr:
            self.addAtTail(val)
        else:
            curr.prev.next, curr.prev, newNode.prev, newNode.next = newNode, newNode, curr.prev, curr
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        
        for _ in range(index):
            if curr.next:
                curr = curr.next
            else:
                return
        if index == 0:
            if self.head.next:
                self.head.next.prev, self.head = None, self.head.next
            else:
                self.head, self.tail = None, None
        elif not curr.next:
            self.tail.prev.next, self.tail = None, self.tail.prev
        else:
            curr.prev.next, curr.next.prev = curr.next, curr.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(indexw


def main():
    linkedList = MyLinkedList()
    print(linkedList.addAtHead(1))
    print(linkedList.addAtTail(3))
    print(linkedList.addAtIndex(1, 2))
    print(linkedList.get(1))
    print(linkedList.deleteAtIndex(1))
    print(linkedList.get(1))

if __name__ == "__main__":
    main()