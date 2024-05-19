class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        char_index = {}

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length
