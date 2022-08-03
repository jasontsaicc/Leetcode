class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        next = [0] * len(s)
        self.getNext(next, s)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False


    def getNext(self, next, s):
        next[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next [i] = j
        return next
