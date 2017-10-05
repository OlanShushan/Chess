from GameObjects import *

class GameMangaer:
    
    Colors = ('Black', 'White')
    blackObjects = []
    whiteObjects = []

    def __init__(self):
        self.chessBoard = ChessBoard()
        self.turnsCounter = 1

    def playTurn(self):
        while not self.hasFinished():
            if self.turnsCounter == 1: 
                self.chessBoard.initCharStartingPositions()
            if(self.turnsCounter % 2 == 0):
                print("White's Turn.")
            else: 
                print("Black's Turn.")
            self.turnsCounter += 1
            self.makeMove()   

    def hasFinished(self):
        for color in GameMangaer.Colors:
            if not self.chessBoard.isKingByColorAlive(color):
                print('{0} Lost!'.format(color))
                return True
        return False

    def makeMove(self, pos1, pos2):
        if not self.canMove(pos1,pos2):
             return
        if Position(pos2).chessPiece != None:
            ChessPiece(Position(pos2).chessPiece).isAlive = False
        Position(pos2).chessPiece = Position(pos1).chessPiece
        Position(pos1).chessPiece = None
     
    def canMove(self, pos1, pos2):
        if not Position.isValid(pos1) or not Position.isValid(pos2) or pos1 == pos2:
            return False
        elif ChessPiece(Position(pos1).chessPiece).color.__eq__(ChessPiece(Position(pos2).chessPiece).color):
            print('Pieces From The Same Team!')
            return
        elif not self.chessBoard.isPositionInBounds(pos1) or not self.chessBoard.inBounds(pos2):
            print('Positions Are Out Of Bounds Of The Board')
            return
        x1 = Position(pos1).x
        y1 = Position(pos1).y
        x2 = Position(pos2).x
        y2 = Position(pos2).y
        if ChessPiece(Position(pos1).chessPiece).char == 'Pawn':
            return {
                'Black' : y2 = y1 + 1,
                'White' : y2 = y1 - 1
            }[ChessPiece(Position(pos1).chessPiece).color] and (abs(x2-x1) == 0 and Position(pos2).chessPiece == None or abs(x2-x1) == 1 and Position(pos2).chessPiece != None)
        else:
            return {
                'King' : (0,1,2).__contains__(abs(y2-y1+x2-x1)) and 
                'Queen' : not self.chessBoard.objectsBetween(pos1, pos2) and 
                'Bishop' : not self.chessBoard.objectsBetween(pos1, pos2) and 
                'Knight' : 
                'Rook' : not self.chessBoard.objectsBetween(pos1, pos2) and 
            }[ChessPiece(Position(pos1).chessPiece).char]