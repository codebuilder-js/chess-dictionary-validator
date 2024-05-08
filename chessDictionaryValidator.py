chessBoard = {'a8': 'r', 'b8': 'n', 'c8': 'b', 'd8': 'k', 'e8': 'q', 'f8': 'b', 'g8': 'n', 'h8': 'r',
              'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p',
              'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
              'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
              'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
              'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
              'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
              'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'K', 'e1': 'Q', 'f1': 'B', 'g1': 'N', 'h1': 'R',}

def printBoard():
    print(f'[{chessBoard['a8']}][{chessBoard['b8']}][{chessBoard['c8']}][{chessBoard['d8']}][{chessBoard['e8']}][{chessBoard['f8']}][{chessBoard['g8']}][{chessBoard['h8']}] 8')
    print(f'[{chessBoard['a7']}][{chessBoard['b7']}][{chessBoard['c7']}][{chessBoard['d7']}][{chessBoard['e7']}][{chessBoard['f7']}][{chessBoard['g7']}][{chessBoard['h7']}] 7')
    print(f'[{chessBoard['a6']}][{chessBoard['b6']}][{chessBoard['c6']}][{chessBoard['d6']}][{chessBoard['e6']}][{chessBoard['f6']}][{chessBoard['g6']}][{chessBoard['h6']}] 6')
    print(f'[{chessBoard['a5']}][{chessBoard['b5']}][{chessBoard['c5']}][{chessBoard['d5']}][{chessBoard['e5']}][{chessBoard['f5']}][{chessBoard['g5']}][{chessBoard['h5']}] 5')
    print(f'[{chessBoard['a4']}][{chessBoard['b4']}][{chessBoard['c4']}][{chessBoard['d4']}][{chessBoard['e4']}][{chessBoard['f4']}][{chessBoard['g4']}][{chessBoard['h4']}] 4')
    print(f'[{chessBoard['a3']}][{chessBoard['b3']}][{chessBoard['c3']}][{chessBoard['d3']}][{chessBoard['e3']}][{chessBoard['f3']}][{chessBoard['g3']}][{chessBoard['h3']}] 3')
    print(f'[{chessBoard['a2']}][{chessBoard['b2']}][{chessBoard['c2']}][{chessBoard['d2']}][{chessBoard['e2']}][{chessBoard['f2']}][{chessBoard['g2']}][{chessBoard['h2']}] 2')
    print(f'[{chessBoard['a1']}][{chessBoard['b1']}][{chessBoard['c1']}][{chessBoard['d1']}][{chessBoard['e1']}][{chessBoard['f1']}][{chessBoard['g1']}][{chessBoard['h1']}] 1')
    print(' A  B  C  D  E  F  G  H')

def isValidBoard(board):
    wKing = 0
    bKing = 0
    wPawn = 0
    bPawn = 0
    wPieces = 0
    bPieces = 0

    for i in board.values():
        if i == 'k':
            wKing += 1
        if i == 'K':
            bKing += 1
        if i == 'p':
            wPawn += 1
        if i == 'P':
            bPawn += 1
        if i.islower():
            wPieces += 1
        if i.isupper():
            bPieces += 1

        if wPieces >= 17 or bPieces >= 17:
            print('TotalPieceError')
            return False
            break

    print('<--- CHESS DICTIONARY VALIDATOR --->')
    print(f' - White King   = [{wKing}/1]')
    print(f' - Black King   = [{bKing}/1]')
    print(f' - White Pawns  = [{wPawn}/8]')
    print(f' - Black Panws  = [{bPawn}/8]')
    print(f' - White Pieces = [{wPieces}/16]')
    print(f' - Black Pieces = [{bPieces}/16]')

    print()
    printBoard()

isValidBoard(chessBoard)