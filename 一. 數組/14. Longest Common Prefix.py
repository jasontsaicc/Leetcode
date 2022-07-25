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

