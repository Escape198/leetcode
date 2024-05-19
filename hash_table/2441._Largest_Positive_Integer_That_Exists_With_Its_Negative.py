class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_positive = -1

        for num in num_set:
            if -num in num_set:
                max_positive = max(max_positive, num)

        return max_positive
