"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""
import heapq

class Solution:
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    def findCheapestPrice(self, n, flights, src, dst, k):
        connections = {}
        for i in range(n):
            connections[i] = []
        
        for flight in flights:
            fligth_src, flight_dst, flight_price = flight
            connections[fligth_src].append((flight_dst, flight_price))
        
        heap = [(0, 0, src, set())]
        heapq.heapify(heap)

        while heap:
            curr_price, curr_k, curr_airport, visit = heap[0]
            heapq.heappop(heap)
            visit.add(curr_airport)

            if curr_airport == dst:
                return curr_price

            if curr_k <= k:
                for neighbor in connections[curr_airport]:
                    neigh_airport, neigh_price = neighbor
                    if neigh_airport not in visit:
                        heapq.heappush(heap, (curr_price + neigh_price, curr_k + 1, neigh_airport, visit.copy()))

        return -1

def main():
    n = 11
    flights = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    src = 0
    dst = 2
    k = 4
    solution = Solution()

    result = solution.findCheapestPrice(n, flights, src, dst, k)
    
    print(result)


if __name__ == "__main__":
    main()