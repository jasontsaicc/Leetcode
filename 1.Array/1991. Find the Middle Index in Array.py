class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        nlen = len(nums)
        sum_nums = sum(nums)
        left = 0
        for i in range(nlen):
            if (sum_nums - nums[i]) - left == left:
                return i
            else:
                left += nums[i]
        return -1