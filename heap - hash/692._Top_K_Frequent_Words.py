class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        sorted_words = sorted(word_count.keys(), key=lambda word: (-word_count[word], word))
        return sorted_words[:k]
