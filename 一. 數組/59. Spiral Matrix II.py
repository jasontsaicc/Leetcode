# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n² in spiral order.
#
#
#  Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
#  Constraints:
#
#
#  1 <= n <= 20
#
#  Related Topics Array Matrix Simulation 👍 3893 👎 187


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 建立一個二維數組 ex n=3 下面代碼會輸出 [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        nums = [[0] * n for _ in range(n)]
        # 定義每循環一個圈的起始位置
        start_x, start_y = 0, 0

        # loop每個圈循環幾次，例如n為奇數3，那麼loop = 1 只是循環一圈，矩陣中間的值需要單獨處理
        # mid矩陣中間的位置，例如：n為3， 中間的位置就是(1，1)，n為5，中間位置為(2, 2)
        loop, mid = n // 2, n // 2
        # 計數
        count = 1

        # 每循環一層偏移量加1，偏移量從1開始
        for offset in range(1, loop + 1):
            # 從左至右，左閉右開
            for i in range(start_y, n - offset):
                nums[start_x][i] = count
                count += 1
            # 從上至下
            for i in range(start_x, n - offset):
                nums[i][n - offset] = count
                count += 1
            # 從右至左
            for i in range(n - offset, start_y, -1):
                nums[n - offset][i] = count
                count += 1
            # 從下至上
            for i in range(n - offset, start_x, -1):
                nums[i][start_y] = count
                count += 1
            # 更新起始點
            start_x += 1
            start_y += 1
        # d
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

# leetcode submit region end(Prohibit modification and deletion)
