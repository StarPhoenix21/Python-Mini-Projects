# Chess Game 

## 🛠️ Description
A simple chess game that you can play with your friend.

## ⚙️ Languages or Frameworks Used
This game is created in python programming language.
Modules : pygame

## 🌟 How to runHow to run the script
Running this game is pretty straight forward.

```sh
pip install -r requirements.txt
```

```sh
python ChessGame.py
```

## 📺 Demo
<p align="center">
<img src="https://github.com/userabhibhullar/python-mini-project/blob/main/IMG/chess.jpg" width=70% height=70%>![alt text]

## 🕹️ Game Instruction
  - Move Pieces: Click on a piece to select it and then click on the target square to move.
  - Undo Moves: Press the 'z' key to undo the last move.
  - Restart Game: Press the 'r' key to restart the game.

## 🎮 Gameplay Features
  - Two-Player Mode: Play with a friend locally.
  - Valid Moves Highlighting: Highlight valid moves for the selected piece.
  - Check and Checkmate Detection: The game detects check and checkmate situations.
  - Stalemate Detection: The game detects stalemate situations.

## 🧩 Classes and Methods
  `GameState`
  - Attributes:
       - board: The current state of the chess board.
       - moveFunctions: A dictionary of piece types and their respective move functions.
       - whiteToMove: Boolean indicating if it's white's turn to move.
       - moveLog: A log of all moves made during the game.
       - whiteKingLocation, blackKingLocation: The current positions of the white and black kings.
       - checkMate, staleMate: Booleans indicating if the game is in checkmate or stalemate.
    
  `Methods`
   - __init__(): Initializes the game state with the starting board setup.
   - makeMove(move): Executes a given move on the board.
   - undoMove(): Undoes the last move made.
   - getValidMoves(): Returns a list of all valid moves, considering checks.
   - inCheck(): Checks if the current player is in check.
   - squareUnderAttack(r, c); Determines if a specific square is under attack.
   - getAllPossibleMoves(): Returns a list of all possible moves without considering checks.
   - getPawnMoves(r, c, moves), getRookMoves(r, c, moves), getKnightMoves(r, c, moves),
     getBishopMoves(r, c, moves), getQueenMoves(r, c, moves), getKingMoves(r, c, moves): Add all
     possible moves for the respective pieces to the list of moves.

  `Move`
  - Attributes:
       - startRow, startCol: The starting position of the move.
       - endRow, andCol: The ending position of the move.
       - pieceMoved, pieceCaptured: The piece being moved and the piece being captured.
       - isPawnPromotion: Whether the move is a pawn promotion.
       - moveID: A unique identifier for the move.

  - Methods:
       - __init__(startSq, endSq, board): Initializes a move object.
       - __eq__(other): Checks if two move objects are equal based on their moveID.
       - getChessNotation(): Returns the move in standard chess notation.
       - getRankFile(r, c,): Converts row and column indicates to chess rank and file notation.

## *Author Name*
[Abhi Bhullar](https://github.com/userabhibhullar)