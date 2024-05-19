class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i, num in enumerate(nums):
            dif = target - nums[i]

            if dif in hash_map:
                return [hash_map[dif], i]
            hash_map[num] = i
