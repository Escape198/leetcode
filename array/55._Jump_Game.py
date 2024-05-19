class Solution:

    def canJump(self, nums: List[int]) -> bool:
        dist = 0

        for i in nums:
            if dist < 0:
                return False
            elif dist < i:
                dist = i
            dist -= 1

        return True
