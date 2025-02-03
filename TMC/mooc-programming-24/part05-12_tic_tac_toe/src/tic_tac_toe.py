# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    if x < 0 or x >= len(game_board[0]) or y < 0 or y >= len(game_board):
        return False
    if game_board[y][x] == "":
        if piece == "X" or piece == "O":
            game_board[y][x] = piece
            return True
    return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)