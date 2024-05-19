class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        max_freq = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            is_valid = r - l + 1 - max_freq <= k
            if not is_valid:
                freq[s[l]] -= 1
                l += 1
        return r - l + 1
