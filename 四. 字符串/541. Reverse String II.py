class Solution:
    def reverseStr(self, s, k):
        from functools import reduce
        # 先把s轉換成list
        s = list(s)

        # 這邊自己使用雙指針 來實作reverse函數
        def reverse(s):
            left, right = 0, len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s
        # make sure we reverse each 2k elements
        for i in range(0, len(s), 2*k):
            s[i:(i+k)] = reverse(s[i:(i+k)])
        # combine list into str.
        return reduce(lambda a, b : a + b , s)

s = Solution()
s.reverseStr(s = "abcdefg", k = 2)