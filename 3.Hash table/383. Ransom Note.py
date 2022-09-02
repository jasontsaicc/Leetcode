class Solution:
    def canConstruct(self, ransomNote, magazine):
        arr = [0] * 26

        for x in magazine:
            arr[ord(x) - ord('a')] += 1

        for i in ransomNote:
            if arr[ord(x) - ord('a')] == 0:
                return False
            else:
                arr[ord(x) - ord('a')] -= 1

            return True
