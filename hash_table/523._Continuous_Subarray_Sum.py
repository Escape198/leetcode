class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        remainder_map = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
            if prefix_sum in remainder_map:
                if i - remainder_map[prefix_sum] > 1:
                    return True
            else:
                remainder_map[prefix_sum] = i

        return False
