"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
"""

class Node:
    
    def __init__(self, val, prev=None, next_=None):
        self.val = val
        self.prev = prev
        self.next = next_

class BrowserHistory:

    def __init__(self, homepage: str): 
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)
        if not self.curr:
            self.curr = newNode
        else:
            self.curr.next = newNode
            newNode.prev = self.curr
            self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.prev:
                break
                
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.next:
                break
                
            self.curr = self.curr.next
        return self.curr.val


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(indexw


def main():
    history = BrowserHistory("leetcode.com")
    print(history.visit("google.com"))
    print(history.visit("facebook.com"))
    print(history.visit("youtube.com"))
    print(history.back(1))
    print(history.back(1))
    print(history.forward(1))
    print(history.visit("linkedin.com"))
    print(history.forward(2))
    print(history.back(2))
    print(history.back(7))

if __name__ == "__main__":
    main()