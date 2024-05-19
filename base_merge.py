def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    p1, p2 = 0, 0
    result = []

    while p1 != len(nums1) or p2 != len(nums2):
        if p2 >= len(nums2) or p1 < len(nums1) and nums1[p1] <= nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
        else:
            result.append(nums2[p2])
            p2 += 1

    return result
