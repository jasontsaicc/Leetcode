# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
#
#
#  Example 1:
#
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
#
#  Example 2:
#
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -10⁴ <= nums[i] <= 10⁴
#  nums is sorted in non-decreasing order.
#
#
#
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach? Related Topics Array
# Two Pointers Sorting 👍 5861 👎 158


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        left_index, right_index, new_list_index = 0, n - 1, n - 1
        ans_list = [1] * n
        while left_index <= right_index:
            lm = nums[left_index] ** 2
            rm = nums[right_index] ** 2
            if lm > rm:
                ans_list[new_list_index] = lm
                left_index += 1
            else:
                ans_list[new_list_index] = rm
                right_index -= 1
            new_list_index -= 1

        return ans_list
s = Solution()
s.sortedSquares([-4,-1,0,3,10])

# leetcode submit region end(Prohibit modification and deletion)
