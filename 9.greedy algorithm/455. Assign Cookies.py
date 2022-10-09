class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #貪心思想+雙指針實現
        #將兩個陣列先排好序
        s.sort()
        g.sort()
        #將兩個指針指向最初位置
        i, j = 0, 0
        #記錄滿足條件的餅乾數量
        count = 0
        while j < len(s) and i < len(g):
            if g[i] <= s[j]:    #小餅乾先喂飽小胃口
                count += 1
                j += 1
                i += 1
            else:
                j += 1
        return count