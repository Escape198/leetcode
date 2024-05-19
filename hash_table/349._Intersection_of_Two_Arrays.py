class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()

        for num in nums2:
            if num in set1:
                result.add(num)
                set1.remove(num)

        return list(result)
