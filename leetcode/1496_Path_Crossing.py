"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

Example 1:

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 
Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""

class Solution:
    # def isPathCrossing(self, path: str) -> bool:
    def isPathCrossing(self, path):
        curr = [0, 0]
        visit = {tuple(curr)}
        
        for p in path:
            if p == "N":
                curr[0] += 1
            elif p == "S":
                curr[0] -= 1
            elif p == "E":
                curr[1] += 1
            else:
                curr[1] -= 1
            if tuple(curr) not in visit:
                visit.add(tuple(curr))
            else:
                return True
        
        return False
            

def main():
    path = "NESWW"

    solution = Solution()

    result = solution.isPathCrossing(path)
    
    print(result)


if __name__ == "__main__":
    main()