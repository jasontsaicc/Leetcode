class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # 1.初始化
        # 2.處理前後綴不相同的情況
        # 3.處理前後缀相同的情况
        # 4.使用next數组来做匹配
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0


    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle))

