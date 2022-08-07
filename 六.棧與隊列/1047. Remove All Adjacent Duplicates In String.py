class Solution:
    def removeDuplicates(self, s):
        # 方法一，使用棧，推薦！
        result = []
        for i in s:
            if result and result[-1] == i:
                result.pop()
            else:
                result.append(i)
        return "".join(result)
    # 方法二，使用雙指針模擬棧，如果不讓用棧可以作為備選方法。
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一樣直接換，不一樣會把後面的填在slow的位置
            res[slow] = res[fast]
            # 如果發現和前一個一樣，就退一格指針
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[0:slow])



# s = Solution()
# s.removeDuplicates(s="abbaca")
