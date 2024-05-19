class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations = set()
        origins = set()

        for origin, destination in paths:
            destinations.add(destination)
            origins.add(origin)

        return (destinations - origins).pop()
