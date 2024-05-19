class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for char in s1:
            count_s1[ord(char) - ord('a')] += 1

        for char in s2[:len_s1]:
            count_s2[ord(char) - ord('a')] += 1

        if count_s1 == count_s2:
            return True

        for i in range(1, len_s2 - len_s1 + 1):
            count_s2[ord(s2[i - 1]) - ord('a')] -= 1
            count_s2[ord(s2[i + len_s1 - 1]) - ord('a')] += 1
            if count_s1 == count_s2:
                return True

        return False