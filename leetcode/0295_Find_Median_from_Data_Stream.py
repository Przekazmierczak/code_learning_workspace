"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import heapq

class MedianFinder:

    def __init__(self):
        self.first_max_heap = []
        heapq.heapify(self.first_max_heap)
        self.second_min_heap = []
        heapq.heapify(self.second_min_heap)

    # def addNum(self, num: int) -> None:
    def addNum(self, num):
        heapq.heappush(self.first_max_heap, -num)
        if len(self.second_min_heap) < len(self.first_max_heap):
            heapq.heappush(self.second_min_heap, -self.first_max_heap[0])
            heapq.heappop(self.first_max_heap)

        if self.first_max_heap and self.second_min_heap:
            if -self.first_max_heap[0] > self.second_min_heap[0]:
                heapq.heappush(self.second_min_heap, -self.first_max_heap[0])
                heapq.heappush(self.first_max_heap, -self.second_min_heap[0])
                heapq.heappop(self.first_max_heap)
                heapq.heappop(self.second_min_heap)

    # def findMedian(self) -> float:
    def findMedian(self):
        if (len(self.first_max_heap) + len(self.second_min_heap)) % 2 == 0:
            return (-self.first_max_heap[0] + self.second_min_heap[0]) / 2
        else:
            return self.second_min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

def main():
    solution = []
    twitter = MedianFinder()
    solution.append(twitter.addNum(-1))
    # solution.append(twitter.findMedian())
    solution.append(twitter.addNum(-2))
    # solution.append(twitter.findMedian())
    solution.append(twitter.addNum(-3))
    # solution.append(twitter.findMedian())
    solution.append(twitter.addNum(-4))
    solution.append(twitter.findMedian())
    # solution.append(twitter.addNum(-5))
    # solution.append(twitter.findMedian())
    # solution.append(twitter.addNum(-6))
    # solution.append(twitter.findMedian())
    
    print(solution)


if __name__ == "__main__":
    main()