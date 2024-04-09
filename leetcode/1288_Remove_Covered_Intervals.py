"""
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
 
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 105
All the given intervals are unique.
"""

class Solution:
    # def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda i: (i[0], -i[1]))
        removed = set()
        
        for curr in range(len(intervals)):
            if curr not in removed:
                i = curr + 1
                while i < len(intervals) and intervals[curr][1] > intervals[i][0]:
                    if intervals[curr][1] >= intervals[i][1]:
                        removed.add(i)
                    i += 1
        
        return len(intervals) - len(removed)
            

def main():
    intervals = [[1,4],[3,6],[2,8]]

    solution = Solution()

    result = solution.removeCoveredIntervals(intervals)
    
    print(result)


if __name__ == "__main__":
    main()