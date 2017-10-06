from GameObjects import *
from BinaryTree import *
from GameRunner import *

level = int
def defineLevel(input):
    if type(input) != int:
        print('Type Error, Level is Int')
        return
    level = input

def firstMethod(board, color):
    if type(board) != ChessBoard : return
    board
    chessPieces = GameMangaer.blackObjects if color == 'Black' GameMangaer.whiteObjects if color == 'White'
    for chessPiece in (board):

def getPossibleMoves(position):
    for x in range(ChessBoard.SQRS_IN_ROW):
        for y in range(ChessBoard.SQRS_IN_ROW):
            