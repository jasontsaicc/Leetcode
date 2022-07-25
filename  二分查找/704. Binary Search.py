# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists, then
# return its index. Otherwise, return -1.
#
#  You must write an algorithm with O(log n) runtime complexity.
#
#
#  Example 1:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
#
#  Example 2:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -10⁴ < nums[i], target < 10⁴
#  All the integers in nums are unique.
#  nums is sorted in ascending order.
#
#  Related Topics Array Binary Search 👍 5646 👎 130


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 定義target在左閉右閉的區間裡，[left, right]
        left, right = 0, len(nums) - 1
        # 當left==right，區間[left, right]依然有效，所以用 <=
        while left <= right:
            # 防止溢出 等同於(left + right)/2
            mid = (left + right) // 2

            # target 在右區間，所以[middle + 1, right]
            if nums[mid] < target:
                left = mid + 1
             # target 在左區間，所以[left, middle - 1]
            elif nums[mid] > target:
                right = mid - 1
            # 數組中找到目標值，直接返回下標
            else:
                return mid
        # 未找到目標值
        return -1

# leetcode submit region end(Prohibit modification and deletion)
