class Solution:
    def canReach(self, arr: List[int], i: int) -> bool:
        if i < 0 or i >= len(arr) or arr[i] < 0: return False
        arr[i] *= -1

        return arr[i] == 0 or self.canReach(arr, i - arr[i]) or self.canReach(arr, i + arr[i])
