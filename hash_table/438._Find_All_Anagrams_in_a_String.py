class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        result = []
        p_freq = {}
        window_freq = {}

        for char in p:
            p_freq[char] = p_freq.get(char, 0) + 1

        for i in range(len(p)):
            window_freq[s[i]] = window_freq.get(s[i], 0) + 1

        if window_freq == p_freq:
            result.append(0)

        for i in range(1, len(s) - len(p) + 1):
            left_char = s[i - 1]
            window_freq[left_char] -= 1
            if window_freq[left_char] == 0:
                del window_freq[left_char]

            right_char = s[i + len(p) - 1]
            window_freq[right_char] = window_freq.get(right_char, 0) + 1

            if window_freq == p_freq:
                result.append(i)

        return result
