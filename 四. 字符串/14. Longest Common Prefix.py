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
#  Related Topics String ð 9020 ð 3173


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # å»ºç«ç©ºçå­ä¸²
        s = ""
        # zip()çç¨æ³
        # å½æ¸ç¨æ¼å°å¯è¿­ä»£çå°è±¡ä½çºåæ¸ï¼å°å°è±¡ä¸­å°æçåç´ æåæä¸åååçµï¼ç¶å¾è¿åç±éäºåçµçµæçå°è±¡
        # å¦æååè¿­ä»£å¨çåç´ åæ¸ä¸ä¸è´ï¼åè¿ååè¡¨é·åº¦èæç­çå°è±¡ç¸å
        for i in zip(*strs):
            # å©ç¨ set çkeyä¸éå¾©çç¹æ§é²è¡å¤æ·
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s
#


# leetcode submit region end(Prohibit modification and deletion)
