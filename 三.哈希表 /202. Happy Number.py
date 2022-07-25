class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(num):
            sum = 0

            # 從個位開始依次取，平方求和
            while num:
                sum += (num % 10) ** 2
                num = num // 10
            return sum

        # 記錄中間結果
        record = set()

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True

            if n in record:
                return False
            else:
                record.add(n)

ans = Solution()
ans.isHappy(2)