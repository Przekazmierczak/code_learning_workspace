"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example 1:

Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Example 2:

Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

Example 3:

Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.
 
Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105
"""
import math

class Solution:
    # def maximumDetonation(self, bombs: List[List[int]]) -> int:
    def maximumDetonation(self, bombs):
        array = [set() for _ in range(len(bombs))]
        for curr in range(len(bombs)):
            for nxt in range(curr + 1, len(bombs)):
                dist = math.sqrt((bombs[curr][0] - bombs[nxt][0]) ** 2 + (bombs[curr][1] - bombs[nxt][1]) ** 2)
                
                if bombs[curr][2] >= dist:
                    array[curr].add(nxt)
                if bombs[nxt][2] >= dist:
                    array[nxt].add(curr)
        

        def dfs(node):
            if node in visit:
                return
            if not array[node]:
                array[node].add(node)
                return
            visit.add(node)
            copy = array[node].copy()
            array[node].add(node)
            for num in copy:
                new_set = dfs(num)
                if new_set:
                    array[node].update(new_set)
            return array[node]
        
        for i in range(len(bombs)):
            visit = set()
            dfs(i)
        
        res = 0
        for node in array:
            res = max(len(node), res)
        return res
            

def main():
    bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]

    solution = Solution()

    result = solution.maximumDetonation(bombs)
    
    print(result)


if __name__ == "__main__":
    main()