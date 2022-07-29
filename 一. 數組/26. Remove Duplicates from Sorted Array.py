class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指針
        # while 結束條件 fast

        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

