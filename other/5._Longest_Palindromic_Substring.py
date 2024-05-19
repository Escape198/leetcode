class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s

        start, size = 0, 1

        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1 = s[l - 1:r]

            if l >= 1 and s1[::-1] == s1:
                size += 2
                start = l - 1
            else:
                s2 = s[l:r]
                if s2[::-1] == s2:
                    size += 1
                    start = l

        return s[start:start + size]
