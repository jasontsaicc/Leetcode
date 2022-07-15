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
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low = s.lower()
        left, right = 0, len(s_low) - 1
        # 判斷只要右指針沒撞到左指針都執行
        while left < right:
            # 使用兩個循環找到左邊和右邊為字母或是數字的位置
            # string.isalnum() 如果 str 至少有一個字符並且所有字符都是字母或數字則返回 True,否則返回 False
            while left < len(s_low) - 1 and not s_low[left].isalnum():
                left += 1
            while right > 0 and not s_low[right].isalnum():
                right -= 1

            # 指針相撞時跳出
            if left >= right:
                break

            else:
                # 如果左右指針所指不同，則肯定不構成回文
                if s_low[left] != s_low[right]:
                    return False
                # 左右指針各前進一步
                else:
                    left += 1
                    right -= 1
        return True


# leetcode submit region end(Prohibit modification and deletion)
