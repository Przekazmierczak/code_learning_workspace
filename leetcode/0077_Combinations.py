"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 
Constraints:

1 <= n <= 20
1 <= k <= n
"""

class Solution:
    # def combine(self, n: int, k: int) -> List[List[int]]:
    def combine(self, n, k):
        ans = []
        
        def result(comb, pointer, k):
            if k == 0:
                ans.append(comb)
            
            for i in range(pointer, n + 1):
                new_comb = comb.copy()
                new_comb.append(i)
                
                if k <= n - i + 1:
                    result(new_comb, i + 1, k - 1)
        
        result([], 1, k)
        return ans
    

def main():
    n = 4
    k = 2

    solution = Solution()

    result = solution.combine(n, k)
    
    print(result)


if __name__ == "__main__":
    main()