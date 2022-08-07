class Solution:
    def removeDuplicates(self, s):
        result = []
        for i in s:
            if result and result[-1] == i:
                result.pop()
            else:
                result.append(i)
        return "".join(result)


# s = Solution()
# s.removeDuplicates(s="abbaca")
