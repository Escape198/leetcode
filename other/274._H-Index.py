class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i, citation in enumerate(citations):
            h_index = max(h_index, min(citation, i + 1))
        return h_index
