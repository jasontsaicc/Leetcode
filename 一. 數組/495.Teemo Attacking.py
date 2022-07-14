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
#  1 <= timeSeries.length <= 10⁴
#  0 <= timeSeries[i], duration <= 10⁷
#  timeSeries is sorted in non-decreasing order.
#
#  Related Topics Array Simulation 👍 478 👎 48


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    def findPoisonedDuration(self, timeSeries, duration):
        # expired = 未中毒的起始時間 ans = 持續中毒時間
        ans, expired = 0, 0
        # 遍歷每個時間點
        # 遭遇第 i 攻擊時
        for i in range(len(timeSeries)):
            # 如果當前他正處於未中毒狀態
            if timeSeries[i] >= expired:
                # 則此時他的中毒持續時間應增加duration
                ans += duration
            # 如果當前他正處於中毒狀態
            else:
                # 上次中毒後結束時間為expired
                # 本次中毒後結束時間為timeSeries[i] + duration
                # 因此本次中毒增加的持續中毒時間為 timeSeries[i] + duration - expired
                ans += timeSeries[i] + duration - expired
            # 我們將每次中毒後增加的持續中毒時間相加即為總的持續中毒時間
            expired = timeSeries[i] + duration
        return ans


s = Solution()
s.findPoisonedDuration([1, 4], 2)

# leetcode submit region end(Prohibit modification and deletion)
