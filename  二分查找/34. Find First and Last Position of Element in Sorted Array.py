# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
#
#  If target is not found in the array, return [-1, -1].
#
#  You must write an algorithm with O(log n) runtime complexity.
#
#
#  Example 1:
#  Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#  Example 2:
#  Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#  Example 3:
#  Input: nums = [], target = 0
# Output: [-1,-1]
#
#
#  Constraints:
#
#
#  0 <= nums.length <= 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#  nums is a non-decreasing array.
#  -10⁹ <= target <= 10⁹
#
#  Related Topics Array Binary Search 👍 11720 👎 315


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            # 記錄一下rightBorder沒有被賦值的情況
            rightBoder = -2
            while left <= right:
                mid = left +(right - left) // 2
                if nums[mid] > target:
                    right =

# leetcode submit region end(Prohibit modification and deletion)
