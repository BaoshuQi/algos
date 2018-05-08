class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        for r in matrix:
            sum = 0
            for i in range(0, len(r)):
                r[i] += sum
                sum = r[i]
        self.m = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for r in range(row1, row2 + 1):
            sum += self.m[r][col2] - self.m[r][col1 - 1] if col1 > 0 else self.m[r][col2]
        return sum
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

obj = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
print(obj)
print(sum([1,0,2]))
print(obj.sumRegion(1,2,2,4))