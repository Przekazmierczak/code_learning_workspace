"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""

class Solution:
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    def findItinerary(self, tickets):
        tickets_dic = {}
        nums_tickets = len(tickets)

        tickets.sort(key=lambda x: x[1])
        
        for ticket in tickets:
            arr, dep = ticket
            if arr not in tickets_dic:
                tickets_dic[arr] = {}
            if dep not in tickets_dic:
                tickets_dic[dep] = {}
            if dep not in tickets_dic[arr]:
                tickets_dic[arr][dep] = 1
            else:
                tickets_dic[arr][dep] += 1
            
        def travel(airport, path, count):
            if count == nums_tickets:
                return path
            for next_flight in tickets_dic[airport]:
                if tickets_dic[airport][next_flight] > 0:
                    path.append(next_flight)
                    tickets_dic[airport][next_flight] -= 1
                    if travel(next_flight, path, count + 1):
                        return path
                    path.pop()
                    tickets_dic[airport][next_flight] += 1
        
        return travel("JFK", ["JFK"], 0)

    
def main():
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    solution = Solution()

    result = solution.findItinerary(tickets)
    
    print(result)


if __name__ == "__main__":
    main()