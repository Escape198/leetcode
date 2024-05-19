class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)

        for key in graph.keys():
            graph[key].sort(reverse=True)
        stack = ["JFK"]
        itinerary = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())

        return itinerary[::-1]
