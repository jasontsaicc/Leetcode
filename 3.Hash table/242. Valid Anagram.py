"""
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

 An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.


 Example 1:
 Input: s = "anagram", t = "nagaram"
Output: true

 Example 2:
 Input: s = "rat", t = "car"
Output: false


 Constraints:


 1 <= s.length, t.length <= 5 * 10⁴
 s and t consist of lowercase English letters.



 Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?

 Related Topics Hash Table String Sorting 👍 5696 👎 232

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        # #並不需要記住字符a的ASCII，只要求出一個相對數值就可以了
        for i in range(len(s)):
            record[ord(s[i]) - ord("a")] += 1
        print(record)
        for i in range(len(t)):
            record[ord(t[i]) - ord("a")] -= 1
            # record數組如果有的元素不為零0，說明字符串s和t 一定是誰多了字符或者誰少了字符。
        for i in range(26):
            if record[i] != 0:
                return False
                # 如果有一個元素不為零，則可以判斷字符串s和t不是字母異位詞
                break
        return Ture




# leetcode submit region end(Prohibit modification and deletion)
