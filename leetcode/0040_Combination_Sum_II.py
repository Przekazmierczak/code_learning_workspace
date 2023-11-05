"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum2(self, candidates, target):
        def check(candidates, target, path, start):
            if target == 0:
                ans.append(path.copy())
                return
                
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    if candidates[i] > target:
                        break
                    current_path = path.copy()
                    current_path.append(candidates[i])
                    check(candidates, target - candidates[i], current_path, i + 1)
        
        candidates.sort()
        ans = []
        check(candidates, target, [], 0)
        
        return ans

def main():
    candidates = [2,5,2,1,2]
    target = 5

    solution = Solution()

    result = solution.combinationSum2(candidates, target)
    
    print(result)


if __name__ == "__main__":
    main()