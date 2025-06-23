def is_valid_chess_board(board):
    piece_counts = {}
    white_king = 0
    black_king = 0

    valid_positions = [f"{r}{c}" for r in '12345678' for c in 'abcdefgh']
    valid_pieces = {
        'wpawn', 'wrook', 'wknight', 'wbishop', 'wqueen', 'wking',
        'bpawn', 'brook', 'bknight', 'bbishop', 'bqueen', 'bking'
    }

    for position, piece in board.items():
        # Validate position
        if position not in valid_positions:
            print(f"Invalid position: {position}")
            return False

        # Validate piece name
        if piece not in valid_pieces:
            print(f"Invalid piece: {piece}")
            return False

        # Count pieces
        piece_counts[piece] = piece_counts.get(piece, 0) + 1
        if piece == 'wking':
            white_king += 1
        elif piece == 'bking':
            black_king += 1

    # Must have exactly one king of each color
    if white_king != 1 or black_king != 1:
        print("Invalid number of kings.")
        return False

    # Optional: Check piece limits
    for piece, count in piece_counts.items():
        if count > 8 and 'pawn' in piece:
            print("Too many pawns.")
            return False
        elif count > 10:
            print(f"Too many pieces of type: {piece}")
            return False

    return True


# Sample chess board
chess_board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'
}

# Test
if is_valid_chess_board(chess_board):
    print("Valid chess board.")
else:
    print("Invalid chess board.")
