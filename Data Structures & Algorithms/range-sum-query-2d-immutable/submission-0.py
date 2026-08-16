class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.arr = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.arr[r+1][c+1] = matrix[r][c]
        # create prefix rows
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.arr[r][c] += self.arr[r][c-1]
        # create prefix squares
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.arr[r][c] += self.arr[r-1][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row_guy = (self.arr[row1][col2 + 1]) - (self.arr[row1][col1])
        col_guy = (self.arr[row2 + 1][col1])

        curr_sum = self.arr[row2 + 1][col2 + 1]

        curr_sum -= row_guy
        curr_sum -= col_guy
        return curr_sum
    


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)