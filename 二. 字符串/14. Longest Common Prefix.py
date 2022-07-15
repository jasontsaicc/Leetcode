# Write a function to find the longest common prefix string amongst an array of
# strings.
#
#  If there is no common prefix, return an empty string "".
#
#
#  Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
#  Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
#  Constraints:
#
#
#  1 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] consists of only lowercase English letters.
#
#  Related Topics String 👍 9020 👎 3173


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 建立空的字串
        s = ""
        # zip()的用法
        # 函數用於將可迭代的對象作為參數，將對象中對應的元素打包成一個個元組，然後返回由這些元組組成的對象
        # 如果各個迭代器的元素個數不一致，則返回列表長度與最短的對象相同
        for i in zip(*strs):
            # 利用 set 的key不重復的特性進行判斷
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s
#


# leetcode submit region end(Prohibit modification and deletion)
