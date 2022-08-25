class Solution:
    def reverseStr(self, s, k):
        # 定義一個交換的函數
        # 'a', 'b' =  'b', 'a'
        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        # res = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        res = list(s)

        # k = 2, range(0, 7, 4) 間隔 4
        # cur = 0, 4, 8
        for cur in range(0, len(s), 2 * k):

            # 調換位置
            #[0 : 0 + 2] = reverse_substring(res[0 : 0 + 2])
            # [4 : 4 + 2] = reverse_substring(res[4 : 4 + 2])
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])

        # bacdfeg
        # print(''.join(res))
        return ''.join(res)

s = Solution()
s.reverseStr(s = "abcdefg", k = 2)