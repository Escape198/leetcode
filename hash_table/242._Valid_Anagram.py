class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            count[char] = count.get(char, 0) - 1

        for val in count.values():
            if val != 0:
                return False

        return True


tracker = defaultdict(int)
for x in s: tracker[x] += 1
for x in t: tracker[x] -= 1
return all(x == 0 for x in tracker.values())
