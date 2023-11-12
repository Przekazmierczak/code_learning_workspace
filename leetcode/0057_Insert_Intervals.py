"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 
Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    def insert(self, intervals, newInterval):
        if intervals == []:
            intervals.append(newInterval)

        last_element = True
        for index in range(len(intervals)):
            if intervals[index][0] >= newInterval[0]:
                last_element = False
                break
        if last_element == True:
            index += 1

        # left
        if index == 0 or intervals[index - 1][1] < newInterval[0]:
            intervals.insert(index, newInterval)
        else:
            intervals[index - 1] = [intervals[index - 1][0], max(newInterval[1], intervals[index - 1][1])]
            index -= 1

        # right
        next_index = index + 1
        max_index = len(intervals)
        while next_index < max_index:
            if intervals[index][1] > intervals[next_index][1]:
                next_index += 1
            else:
                if intervals[index][1] < intervals[next_index][0]:
                    intervals = intervals[:index + 1] + intervals[next_index:]
                else:
                    intervals[index] = [intervals[index][0], intervals[next_index][1]]
                    intervals = intervals[:index + 1] + intervals[next_index + 1:]
                break

        if next_index == max_index:
            intervals = intervals[:index + 1]
        
        return intervals



def main():
    intervals = [[1, 5], [6, 9], [10, 12], [15, 19], [20, 22], [25, 27]]
    newInterval = [28,29]

    solution = Solution()

    result = solution.insert(intervals, newInterval)
    
    print(result)


if __name__ == "__main__":
    main()