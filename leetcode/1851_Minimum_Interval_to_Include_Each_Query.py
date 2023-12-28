"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.

Constraints:

1 <= intervals.length <= 105
1 <= queries.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107
"""
import heapq

class Solution:
    # def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    def minInterval(self, intervals, queries):
        queries_with_positions = []
        for i in range(len(queries)):
            queries_with_positions.append((queries[i], i))

        intervals.sort()
        queries_with_positions.sort()

        heap = []
        heapq.heapify(heap)
        result = [0 for _ in range(len(queries))]

        queries_pointer = 0
        intervals_pointer = 0

        while queries_pointer < len(queries_with_positions):
            while intervals_pointer < len(intervals) and intervals[intervals_pointer][0] <= queries_with_positions[queries_pointer][0]:
                size = intervals[intervals_pointer][1] - intervals[intervals_pointer][0] + 1
                heapq.heappush(heap, (size, intervals[intervals_pointer][1]))
                intervals_pointer += 1

            while heap and heap[0][1] < queries_with_positions[queries_pointer][0]:
                heapq.heappop(heap)

            if heap:
                result[queries_with_positions[queries_pointer][1]] = heap[0][0]
            else:
                result[queries_with_positions[queries_pointer][1]] = -1

            queries_pointer += 1

        return result
        

def main():
    intervals = [[4,5],[5,8],[1,9],[8,10],[1,6]]
    queries = [7,9,3,9,3]

    solution = Solution()

    result = solution.minInterval(intervals, queries)
    
    print(result)


if __name__ == "__main__":
    main()