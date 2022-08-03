class Solution:
    def reverseStr(self, s, k):
        # 定義一個交換的函數
        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        #
        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])

        return ''.join(res)

s = Solution()
s.reverseStr(s = "abcdefg", k = 2)