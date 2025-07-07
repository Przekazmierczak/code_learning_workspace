/*
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation:
version1 has less revisions, which means every missing revision are treated as "0".

Constraints:
1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
*/

#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> create_vector(std::string version) {
        std::string curr = "";
        std::vector<int> res;
        for (int i = 0; i < version.size(); i++) {
            if (version[i] == '.') {
                res.push_back(stoi(curr));
                curr = "";
            } else {
                curr += version[i];
            }
        }
        res.push_back(stoi(curr));
        return res;
    }
    
    int compareVersion(std::string version1, std::string version2) {
        std::vector<int> v1 = create_vector(version1);
        std::vector<int> v2 = create_vector(version2);
        
        while (v1.size() > v2.size()) v2.push_back(0);
        while (v2.size() > v1.size()) v1.push_back(0);
        for (int i = 0; i < v1.size(); i++) {
            if (v1[i] > v2[i]) return 1;
            if (v2[i] > v1[i]) return -1;
        }
        return 0;
    }
};