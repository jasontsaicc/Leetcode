# coding=utf-8
# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo
# attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an
# attack at second t will mean Ashe is poisoned during the inclusive time interval
# [t, t + duration - 1]. If Teemo attacks again before the poison effect ends,
# the timer for it is reset, and the poison effect will end duration seconds after
# the new attack.
#
#  You are given a non-decreasing integer array timeSeries, where timeSeries[i]
# denotes that Teemo attacks Ashe at second timeSeries[i], and an integer
# duration.
#
#  Return the total number of seconds that Ashe is poisoned.
#
#
#  Example 1:
#
#
# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
#
#
#  Example 2:
#
#
# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe
# is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
#
#
#  Constraints:
#
#
#  1 <= timeSeries.length <= 10β΄
#  0 <= timeSeries[i], duration <= 10β·
#  timeSeries is sorted in non-decreasing order.
#
#  Related Topics Array Simulation π 478 π 48


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    # def findPoisonedDuration(self, timeSeries, duration):
    #     # expired = ζͺδΈ­ζ―ηθ΅·ε§ζι ans = ζηΊδΈ­ζ―ζι
    #     ans, expired = 0, 0
    #     # ιζ­·ζ―εζιι»
    #     # ι­ιη¬¬ i ζ»ζζ
    #     for i in range(len(timeSeries)):
    #         # ε¦ζηΆεδ»ζ­£θζΌζͺδΈ­ζ―ηζ
    #         if timeSeries[i] >= expired:
    #             # εζ­€ζδ»ηδΈ­ζ―ζηΊζιζε’ε duration
    #             ans += duration
    #         # ε¦ζηΆεδ»ζ­£θζΌδΈ­ζ―ηζ
    #         else:
    #             # δΈζ¬‘δΈ­ζ―εΎη΅ζζιηΊexpired
    #             # ζ¬ζ¬‘δΈ­ζ―εΎη΅ζζιηΊtimeSeries[i] + duration
    #             # ε ζ­€ζ¬ζ¬‘δΈ­ζ―ε’ε ηζηΊδΈ­ζ―ζιηΊ timeSeries[i] + duration - expired
    #             ans += timeSeries[i] + duration - expired
    #         # ζεε°ζ―ζ¬‘δΈ­ζ―εΎε’ε ηζηΊδΈ­ζ―ζιηΈε ε³ηΊηΈ½ηζηΊδΈ­ζ―ζι
    #         expired = timeSeries[i] + duration
    #     return ans

    def findPoisonedDuration(self, timeSeries, duration):
        #
        for i in range(len(timeSeries) - 1):
            timeSeries[i] = min(timeSeries[i + 1]-timeSeries[i], duration)
        return sum(timeSeries[:-1]) + duration

s = Solution()
s.findPoisonedDuration([1, 4], 2)

# leetcode submit region end(Prohibit modification and deletion)
