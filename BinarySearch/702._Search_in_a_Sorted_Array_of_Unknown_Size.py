class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 10000
        while left <= right:
            mid = (left + right)//2
            val = reader.get(mid)

            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
