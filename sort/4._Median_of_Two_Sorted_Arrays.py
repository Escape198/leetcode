class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2 == 0:
            mid1 = len(nums) // 2
            mid2 = mid1 - 1
            return (nums[mid1] + nums[mid2]) / 2
        else:
            return nums[len(nums) // 2]
