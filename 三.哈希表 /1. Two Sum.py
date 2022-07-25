"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

 You may assume that each input would have exactly one solution, and you may
not use the same element twice.

 You can return the answer in any order.


 Example 1:


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


 Example 2:


Input: nums = [3,2,4], target = 6
Output: [1,2]


 Example 3:


Input: nums = [3,3], target = 6
Output: [0,1]



 Constraints:


 2 <= nums.length <= 10⁴
 -10⁹ <= nums[i] <= 10⁹
 -10⁹ <= target <= 10⁹
 Only one valid answer exists.



Follow-up: Can you come up with an algorithm that is less than
O(n²) time complexity?

 Related Topics Array Hash Table 👍 35139 👎 1117

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums, target):
        records = {}
        for i in range(len(nums)):
            # 直接相減 如果[3,2,4], target = 6 就是6去減3 再去dict找3

            rest = target - nums[i]

            if records.get(rest) is None:
                # 如果沒找到匹配對，就把訪問過的元素和下標加入到record中
                records[nums[i]] = i
                continue
            # 找到了 就回傳index
            return [records[rest], i]
s = Solution()
s.twoSum([2,7,11,15], 9)
# leetcode submit region end(Prohibit modification and deletion)
