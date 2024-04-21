"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
"""

class Node:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.currSize = 0
        self.maxSize = k
        self.gate = Node(None)

    def enQueue(self, value: int) -> bool: 
        if self.currSize == self.maxSize:
            return False
        newNode = Node(value)
        if self.currSize == 0:
            self.gate.next, self.gate.prev = newNode, newNode
            newNode.next, newNode.prev = self.gate, self.gate
        else:
            newNode.prev, newNode.next = self.gate, self.gate.next
            self.gate.next.prev, self.gate.next = newNode, newNode
        self.currSize += 1
        return True

    def deQueue(self) -> bool:
        if self.currSize == 0:
            return False
        if self.currSize == 1:
            self.gate.next, self.gate.prev = None, None
        else:
            self.gate.prev.prev.next, self.gate.prev = self.gate, self.gate.prev.prev
        self.currSize -= 1
        return True
        

    def Front(self) -> int:
        return self.gate.prev.val if self.currSize > 0 else -1

    def Rear(self) -> int:
        return self.gate.next.val if self.currSize > 0 else -1

    def isEmpty(self) -> bool:
        return True if self.currSize == 0 else False

    def isFull(self) -> bool:
        return True if self.currSize == self.maxSize else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

def main():
    que = MyCircularQueue(3)
    print(que.enQueue(1))
    print(que.enQueue(2))
    print(que.enQueue(3))
    print(que.enQueue(4))
    print(que.Rear())
    print(que.isFull())
    print(que.deQueue())
    print(que.enQueue(4))
    print(que.Rear())

if __name__ == "__main__":
    main()