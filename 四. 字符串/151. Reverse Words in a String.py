class Solution:
    # 1.去除多餘的空格
    # 2.翻轉字符串
    # 3.翻轉每個單詞

    # 1.去除多餘的空格
    def trim_spaces(self, s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == ' ':  # 去除開頭的空格
            left += 1
        while left <= right and s[right] == ' ':  # 去除結尾的空格
            right = right - 1
        tmp = []
        while left <= right:  # 去除單詞中間多餘的空格
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':  # 當前位置是空格，但是相鄰的上一個位置不是空格，則該空格是合理的
                tmp.append(s[left])
            left += 1
        return tmp

    # 2.翻轉字符數組
    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None

    # 3.翻轉每個單詞
    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums, start, end - 1)
            start = end + 1
            end += 1
        return None

    # 4.翻轉字符串裡的單詞
    def reverseWords(self, s):  # 測試用例："the sky is blue"
        l = self.trim_spaces(s)  # 輸出：['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'
        self.reverse_string(l, 0,
                            len(l) - 1)  # 輸出：['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
        self.reverse_each_word(l)  # 輸出：['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
        return ''.join(l)  # 輸出：blue is sky the

