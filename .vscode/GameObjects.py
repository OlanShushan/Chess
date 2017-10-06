class ChessPiece:

    chessPiecesCounter = 0
    
    def __init__(self, char = '', color = ''):
        self.__character = char
        self.__color = color
        self.__isAlive = True
        ChessPiece.chessPiecesCounter += 1

    @property
    def char(self):
        return self.__character
    @char.setter
    def char(self, value):
        self.__character = value

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value
    
    @property
    def isAlive(self):
        return self.__isAlive
    @isAlive.setter
    def isAlive(self, value):
        self.__isAlive = value

    def __str__(self):
        return '({0},{1},{2})'.format(self.__character, self.__color, 'Alive' if self.__isAlive else 'Dead')

class ChessBoard:

    SQRS_IN_ROW = 8
    WHITE_PAWNS_ROW = 1
    BLACK_PAWNS_ROW = 6
    WHITE_NOBILITY_ROW = 0
    BLACK_NOBILITY_ROW = 7

    def __init__(self):
        self.positionsTable = []
        self.initPositions()

    def initPositions(self):
        for i in range(ChessBoard.SQRS_IN_ROW):
            row = []
            for j in range(ChessBoard.SQRS_IN_ROW):
                row.append(Position(i+1,j+1))
            self.positionsTable.append(row)

    def initCharStartingPositions(self):
        for i in range(ChessBoard.SQRS_IN_ROW):
            Position(self.positionsTable[ChessBoard.WHITE_PAWNS_ROW][i]).chessPiece = ChessPiece("Pawn", 'White')
        for i in range(ChessBoard.SQRS_IN_ROW):
            Position(self.positionsTable[ChessBoard.WHITE_NOBILITY_ROW][i]).chessPiece = {
                0 : ChessPiece('Rook', 'White'),
                1 : ChessPiece('Knight', 'White'),
                2 : ChessPiece('Bishop', 'White'),
                3 : ChessPiece('Queen', 'White'),
                4 : ChessPiece('King', 'White'),
                5 : ChessPiece('Bishop', 'White'),
                6 : ChessPiece('Knight', 'White'),
                7 : ChessPiece('Rook', 'White')
            }[i]
        for i in range(ChessBoard.SQRS_IN_ROW):
                Position(self.positionsTable[ChessBoard.BLACK_PAWNS_ROW][i]).chessPiece = ChessPiece("Pawn", 'Black')
        for i in range(ChessBoard.SQRS_IN_ROW):
            Position(self.positionsTable[ChessBoard.BLACK_NOBILITY_ROW][i]).chessPiece = {
                0 : ChessPiece('Rook', 'Black'),
                1 : ChessPiece('Knight', 'Black'),
                2 : ChessPiece('Bishop', 'Black'),
                3 : ChessPiece('Queen', 'Black'),
                4 : ChessPiece('King', 'Black'),
                5 : ChessPiece('Bishop', 'Black'),
                6 : ChessPiece('Knight', 'Black'),
                7 : ChessPiece('Rook', 'Black')
            }[i]
    
    def countAliveByColor(self, color):
        counter = 0
        for i in range(ChessBoard.SQRS_IN_ROW):
            for j in range(ChessBoard.SQRS_IN_ROW):
                if ChessPiece(Position(self.positionsTable[i][j]).chessPieces).color.__eq__(color) and ChessPiece(Position(self.positionsTable[i][j]).chessPiece).isAlive:
                    counter += 1
        return counter

    def isKingByColorAlive(self, color):
        aliveKing = ChessPiece('King', color, True)
        for i in range(ChessBoard.SQRS_IN_ROW):
            for j in range(ChessBoard.SQRS_IN_ROW):
                if not Position(self.positionsTable[i][j]).chessPieces.__eq__(aliveKing):
                    return False
        return True

    def isPositionInBounds(self, position):
        if not Position.isValid(position):
            return
        return Position(position).x > 0 and Position(position).x < ChessBoard.SQRS_IN_ROW and Position(position).y > 0 and Position(position).y < ChessBoard.SQRS_IN_ROW

    def objectsBetween(self, pos1, pos2):
        if not Position.isValid(pos1) or not Position.isValid(pos2) or pos1.__eq__(pos2):
            return False
        x1 = Position(pos1).x
        y1 = Position(pos1).y
        x2 = Position(pos2).x
        y2 = Position(pos2).y
        xDiff = x2 - x1
        yDiff = y2 - y1
        if xDiff == yDiff:
            for i in range(x1+1,x2-1):
                if not Position(self.positionsTable[i][i]).isEmpty():
                    return True
        elif xDiff > 0 and yDiff == 0:
            for i in range(x1+1,x2-1):
                if not Position(self.positionsTable[i][y1]).isEmpty():
                    return True
        elif yDiff > 0 and xDiff == 0:
            for i in range(y1+1,y2-1):
                if not Position(self.positionsTable[x1][i]).isEmpty():
                    return True
        return False
 
    def printBoard(self):
        for i in range(ChessBoard.SQRS_IN_ROW):
            row = ''
            for j in range(ChessBoard.SQRS_IN_ROW):
                row += '[{0} : {1}]'.format(self.positionsTable[i][j].__str__(),ChessPiece(Position(self.positionsTable[i][j]).chessPiece).char)
            print(row)

    
class Position:

    def __init__(self, x=-1, y=-1):
        self.x = x
        self.y = y
        self.chessPiece = None

    def isEmpty(self):
        return self.chessPiece == None

    @classmethod
    def isValid(self, position):
        return position and type(position) == Position

    def __str__(self):
        return '({0},{1})'.format(self.x, self.y)
