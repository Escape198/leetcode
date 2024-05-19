class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1

        for d in range(m + n - 1, -1, -1):
            if p2 < 0:
                return

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[d] = nums1[p1]
                p1 -= 1
            else:
                nums1[d] = nums2[p2]
                p2 -= 1