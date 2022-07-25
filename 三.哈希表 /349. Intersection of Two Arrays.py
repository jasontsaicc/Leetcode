class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 兩個數組先變成集合，求交集後還原為數組
        return list(set(nums1) & set(nums2))