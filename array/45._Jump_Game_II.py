class Solution:

    def jump(self, nums: List[int]) -> int:
        reach, count, last = 0, 0, 0

        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])

            if i == last:
                last = reach

                count += 1

        return count
