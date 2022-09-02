# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1,
# numsr] of which the sum is greater than or equal to target. If there is no such
# subarray, return 0 instead.
#
#
#  Example 1:
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
#
#
#  Example 2:
#
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
#
#  Example 3:
#
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
#
#  Constraints:
#
#
#  1 <= target <= 10⁹
#  1 <= nums.length <= 10⁵
#  1 <= nums[i] <= 10⁴
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)). Related Topics Array Binary
# Search Sliding Window Prefix Sum 👍 7173 👎 207


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target, nums):
        # 最終的結果
        result = len(nums) + 1
        # 滑動窗口數值之和
        sum = 0
        # 滑動窗口起始位置
        index = 0
        for i in range(len(nums)):
            sum += nums[i]
            # 使用while，每次更新 i（起始位置），並不斷比較子序列是否符合條件
            while sum >= target:
                # 取子序列的長度
                result = min(result, i-index+1)
                # 這裡體現出滑動窗口的精髓之處，不斷變更i（子序列的起始位置）
                sum -= nums[index]
                index += 1
        # 如果result沒有被賦值的話，就返回0，說明沒有符合條件的子序列
        return 0 if result == len(nums) + 1 else result

s=Solution()
s.minSubArrayLen(7,[2,3,1,2,4,3])

# leetcode submit region end(Prohibit modification and deletion)
