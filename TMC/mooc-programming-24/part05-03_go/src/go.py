# Write your solution here
def who_won(game_board: list) -> int:
    black = 0
    white = 0
    for baris in game_board:
        black += baris.count(1)
        white += baris.count(2)
    if black == white:
        return 0
    elif black > white:
        return 1
    else:
        return 2
    
if __name__ == "__main__":
    go = [
      [9, 0, 0, 0, 8, 0, 3, 0, 0],
      [0, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [0, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(who_won(go))