"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the same
forward and backward. Alphanumeric characters include letters and numbers.

 Given a string s, return true if it is a palindrome, or false otherwise.


 Example 1:


Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


 Example 2:


Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


 Example 3:


Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.

Since an empty string reads the same forward and backward, it is a palindrome.



 Constraints:


 1 <= s.length <= 2 * 10β΅
 s consists only of printable ASCII characters.


 Related Topics Two Pointers String π 4266 π 5621

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # εε»ζη©Ίζ Ό εθ½ηΊε°ε―«
        s = s.replace(" ", "").lower()
        # δ½Ώη¨ιζι
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                print("False")
                return False
        print("True")
        return True


s = Solution()
s.isPalindrome( "A man, a plan, a canal: Panama")

# leetcode submit region end(Prohibit modification and deletion)
