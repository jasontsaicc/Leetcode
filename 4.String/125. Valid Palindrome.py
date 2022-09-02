# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include letters and numbers.
#
#  Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#  Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
#  Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
#  Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 2 * 10⁵
#  s consists only of printable ASCII characters.
#
#  Related Topics Two Pointers String 👍 4156 👎 5548


# leetcode submit region begin(Prohibit modification and deletion)

"""
可以用正則 也可以用雙指針,
1.先把” ”去除以及轉小寫
2.設定左右指針(注意右邊index)
3.使用while 判斷 執行條件 left < right
4.如果left指針的值 == right的值 個別往前往後,
5. 如果遇到不是isalnum() 左邊往前,
6. 如果遇到不是isalnum() 右邊往後,
7. 回傳False,
8while 回傳True
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','').lower()
        left,right = 0, len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
