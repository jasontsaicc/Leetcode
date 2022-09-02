"""
請實現一個函數，把字符串 s 中的每個空格替換成"%20"。
示例 1：

輸入：s = "We are happy."
輸出："We%20are%20happy."""

class Solution:
    def replaceSpace(self, s):
        counter = s.count(" ")

        result = list(s)
        # 每碰到一個空格就多拓展兩個格子，1 + 2 = 3個位置存’%20‘
        result.extend([" "] * counter * 2)

        left, right = len(s) - 1, len(result) - 1

        while left >= 0:
            if result[left] != " ":
                result[right] = result[left]
                right -= 1
            else:
                result[right - 2: right + 1] = "%20"
                right -= 3
            left -= 1
        return "".join(result)