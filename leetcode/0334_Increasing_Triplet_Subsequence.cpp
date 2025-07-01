/*
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
*/

#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    bool increasingTriplet(std::vector<int>& nums) {
        int minSingle = INT_MAX;
        int minDuble = INT_MAX;

        for (int& num : nums) {
            if (num > minDuble) return true;
            if (num > minSingle) minDuble = num;
            if (num < minSingle) minSingle = num;
        }
        return false;
    }
};