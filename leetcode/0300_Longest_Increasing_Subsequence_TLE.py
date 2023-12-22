"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
1 <= nums[i] <= 100
"""

class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums):
        def bianary_search(sublist, value):
            left = 0
            right = len(sublist) - 1

            while left <= right:
                mid = (left + right) // 2

                if sublist[mid] < value:
                    left = mid + 1
                elif sublist[mid] > value:
                    right = mid - 1
                else:
                    return -1
            return right

        sublists = []
        sublists.append([nums[0]])

        for i in range(1, len(nums)):
            for j in range(len(sublists)):
                if sublists[j][-1] < nums[i]:
                    sublists[j].append(nums[i])
                elif sublists[j][0] < nums[i] < sublists[j][-1]:
                    sublist_index = bianary_search(sublists[j], nums[i])
                    new_sublist = sublists[j][:sublist_index + 1]
                    new_sublist.append(nums[i])
                    if new_sublist not in sublists:
                        sublists.append(new_sublist)
                elif sublists[j][0] > nums[i] and len(sublists[j]) == 1:
                    sublists.remove(sublists[j])
            if [nums[i]] not in sublists:
                sublists.append([nums[i]])

        return len(max(sublists, key=len))

def main():
    nums = [-813,82,-728,-82,-432,887,-551,324,-315,306,-164,-499,-873,-613,932,177,61,52,1000,-710,372,-306,-584,-332,-500,407,399,-648,290,-866,222,562,993,-338,-590,303,-16,-134,226,-648,909,582,177,899,-343,55,629,248,333,1,-921,143,629,981,-435,681,844,349,613,457,797,695,485,15,710,-450,-775,961,-445,-905,466,942,995,-289,-397,434,-14,34,-903,314,862,-441,507,-966,525,624,-706,39,152,536,874,-364,747,-35,446,-608,-554,-411,987,-354,-700,-34,395,-977,544,-330,596,335,-612,28,586,228,-664,-841,-999,-100,-620,718,489,346,450,772,941,952,-560,58,999,-879,396,-101,897,-1000,-566,-296,-555,938,941,475,-260,-52,193,379,866,226,-611,-177,507,910,-594,-856,156,71,-946,-660,-716,-295,-927,148,620,201,706,570,-659,174,637,-293,736,-735,377,-687,-962,768,430,576,160,577,-329,175,51,699,-113,950,-364,383,5,748,-250,-644,-576,-227,603,832,-483,-237,235,893,-336,452,-526,372,-418,356,325,-180,134,-698]

    solution = Solution()

    result = solution.lengthOfLIS(nums)
    
    print(result)


if __name__ == "__main__":
    main()