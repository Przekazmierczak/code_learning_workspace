"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""

class Node:
    def __init__(self):
        self.exist = False
        self.nxt = [None] * 10

class MyHashSet:
    def __init__(self):
        self.hash = Node()

    # def add(self, key: int) -> None:
    def add(self, key):
        curr = self.hash
        while key:
            num = key % 10
            if not curr.nxt[num]:
                curr.nxt[num] = Node()
            curr = curr.nxt[num]
            key = key // 10
        curr.exist = True

    # def remove(self, key: int) -> None:
    def remove(self, key):
        curr = self.hash
        while key:
            num = key % 10
            if curr.nxt[num]:
                curr = curr.nxt[num]
            else:
                return
            key = key // 10
        curr.exist = False

    # def contains(self, key: int) -> bool:
    def contains(self, key):
        curr = self.hash
        while key:
            num = key % 10
            if not curr.nxt[num]:
                return False
            else:
                curr = curr.nxt[num]
            key = key // 10
        return True if curr.exist else False    
            

def main():
    hash_set = MyHashSet()
    print(hash_set)
    print(hash_set.add(1))
    print(hash_set.add(2))
    print(hash_set.contains(1))
    print(hash_set.contains(3))
    print(hash_set.add(2))
    print(hash_set.contains(2))
    print(hash_set.remove(2))
    print(hash_set.contains(2))
    
if __name__ == "__main__":
    main()