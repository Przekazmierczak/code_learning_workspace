/*
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
*/

#include <vector>
#include <array>

class Solution {
public:
    int dominantIndex(std::vector<int>& nums) {
        std::array<int, 101> arr;
        arr.fill(-1);
        int largest = -1;
        
        for (int i = 0; i < nums.size(); i++) {
            arr[nums[i]] = i;
        }
        
        for (int i = arr.size() - 1; i >= 0; i--) {
            if (arr[i] != -1) {
                if (largest == -1) {
                    largest = i;
                } else {
                    return largest >= i*2 ? arr[largest] : -1;
                }
            }
        }
        return -1;
    }
};