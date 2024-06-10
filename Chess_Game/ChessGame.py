import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSIONS = 8
SQ_SIZE = HEIGHT// DIMENSIONS
MAX_FPS = 15
IMAGES = {}

def loadImages():
    """
    Load chess piece images and scale them to the appropriate size.
    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK' ]
    for piece in pieces: 
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    """
    Main function to run the chess game.

    This function initializes the game window, sets up the game state, handles user input,
    updates the game state based on user actions, and renders the game state on the screen.
    """
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    animate = False
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    gameOver = False
    while running: 
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if sqSelected == (row, col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 1 and (gs.board[row][col] == "--"): 
                        sqSelected = ()
                        playerClicks = []
                    if len(playerClicks) == 2:
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(move)
                                moveMade = True
                                animate = True
                                sqSelected = ()
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    animate = False
                if e.key == p.K_r:
                    gs = ChessEngine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
        if moveMade:
            if animate:
                animatedMoves(gs.moveLog[-1], screen, gs.board,clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False
        drawGameState(screen, gs, validMoves, sqSelected)
        if gs.checkMate:
            gameOver = True
            if gs.whiteToMove:
                drawText(screen, 'Black wins by checkmate')
            else:
                drawText(screen, 'White wins by checkmate')
        elif gs.staleMate:
            gameOver =True
            drawText(screen, 'Stalemate');
        clock.tick(MAX_FPS)
        p.display.flip()

def highlightSquares(screen, gs, validMoves, sqSelected):
    """
    Highlight the squares on the chessboard based on the selected piece and its valid moves.

    Args:
        screen: The game screen surface.
        gs (ChessEngine.GameState): The current game state.
        validMoves (list): List of valid moves for the selected piece.
        sqSelected (tuple): Tuple containing the coordinates of the selected square.
    """
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(p.Color('blue'))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            s.fill(p.Color("yellow"))
            for moves in validMoves:
                if moves.startRow == r and moves.startCol == c:
                    screen.blit(s, (SQ_SIZE*moves.endCol, SQ_SIZE*moves.endRow))

def drawGameState(screen, gs, validMoves, sqSelected):
    """
    Draw the current state of the chess game on the screen.

    Args:
        screen: The game screen surface.
        gs (ChessEngine.GameState): The current game state.
        validMoves (list): List of valid moves for the selected piece.
        sqSelected (tuple): Tuple containing the coordinates of the selected square.
    """
    drawBoard(screen)
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    """
    Draw the chessboard on the screen.

    Args:
        screen: The game screen surface.
    """
    global colors
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    """
    Draw the chess pieces on the screen based on the current board state.

    Args:
        screen: The game screen surface.
        board (list): 2D list representing the class board state.
    """
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def animatedMoves(move, screen,board, clock):
    """
    Animate the movement of a chess piece on the screen.

    Args:
        move (ChessEngine.Move): The move to animate.
        screen: The game screen surface.
        board (list): 2D list representing the chess board state.
        clock: Pygame clock objects.
    """
    global colors
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 5
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount + 1):
        r,c =((move.startRow + dR*frame/frameCount, move.startCol + dC*frame/frameCount))
        drawBoard(screen)
        drawPieces(screen, board)
        color = colors[(move.endRow + move.endCol)%2]
        endSquare = p.Rect(move.endCol*SQ_SIZE, move.endRow*SQ_SIZE, SQ_SIZE, SQ_SIZE)
        p.draw.rect(screen, color, endSquare)
        if move.pieceCaptured != "--":
            screen.blit(IMAGES[move.pieceCaptured], endSquare)

        screen.blit(IMAGES[move.pieceMoved], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        p.display.flip()
        clock.tick(60)

def drawText(screen, text):
    """
    Draw text on the screen

    Args:
        screen: The game screen surface.
        text (str): The text to be displayed.
    """
    font = p.font.SysFont("Helvitca", 32, True, False)
    textObject = font.render(text, True, p.Color('Gray'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)
    textObject = font.render(text, True, p.Color("Black"))
    screen.blit(textObject, textLocation.move(2,2))


if __name__ == "__main__":
    main()
