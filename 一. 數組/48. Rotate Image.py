class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.

        # 順時針反轉九十度可以分成兩步
        1.先對角線翻轉
        2.接著進行列方向的逆序

        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
