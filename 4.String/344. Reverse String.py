class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 這裡使用雙指針
        left, right = 0, len(s) - 1
        # 注意 這裡是小於不是小於等於 邊界設置 左閉右開
        while left < right:
            # 直接做交換
            s[left], s[right] = s[right], s[left]
            # 左指針往前一格
            left += 1
            # 右指針往後一格
            right -= 1