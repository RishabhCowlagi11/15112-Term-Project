class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[None] * self.cols for i in range(self.rows)]

    # @static
    # def print2dList(L):
    #     for i in L:
    #         print(i)

    def displayBoard(self):
        print2dList(self.board)

    