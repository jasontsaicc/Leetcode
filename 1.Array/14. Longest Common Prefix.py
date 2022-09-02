"""
Write a function to find the longest common prefix string amongst an array of
strings.

 If there is no common prefix, return an empty string "".


 Example 1:


Input: strs = ["flower","flow","flight"]
Output: "fl"


 Example 2:


Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



 Constraints:


 1 <= strs.length <= 200
 0 <= strs[i].length <= 200
 strs[i] consists of only lowercase English letters.


 Related Topics String 👍 9199 👎 3211

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""

        for i in zip(*strs):
            # 其中的第 i 個元組包含來自每個參數序列或可迭代對象的第 i 個元素
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s



# leetcode submit region end(Prohibit modification and deletion)



