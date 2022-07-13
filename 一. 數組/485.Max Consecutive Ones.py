# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
#
#
#  Example 1:
#
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#  The maximum number of consecutive 1s is 3.
#
#
#  Example 2:
#
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁵
#  nums[i] is either 0 or 1.
#
#  Related Topics Array 👍 2930 👎 404


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    def findMaxConsecutiveOnes(self, nums):
        # 為了得到數組中最大連續 1的個數，需要遍歷數組，
        # 並記錄最大的連續 1 的個數和當前的連續 1 的個數
        maxcount = 0
        count = 0
        for i, num in enumerate(nums):
            # 如果當前元素是1，則將當前的連續 1 的個數加 1
            if num == 1:
                count += 1
                
            #否則，使用之前的連續 1 的個數更新最大的連續 1 的個數
            # 並將當前的連續 1 的個數清零。
            else:
                maxcount = max(maxcount, count)
                count = 0

        # 因為數組的最後一個元素可能是 1，且最長連續 1 的子數組可能出現在數組的末尾，
        # 如果遍歷數組結束之後不更新最大的連續 11 的個數，則會導致結果錯誤
        maxcount = max(maxcount, count)
        return maxcount
s = Solution()
s.findMaxConsecutiveOnes([1,1,0,1,1,1])


# leetcode submit region end(Prohibit modification and deletion)
