import random

def initialize_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows) for _ in range(rows)]
    mine_positions = random.sample(range(rows * cols), mines)

    for mine_pos in mine_positions:
        row = mine_pos // cols
        col = mine_pos % cols
        board[row][col] = 'X'

    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_adjacent_mines(board, row, col):
    mine_count = 0
    rows, cols = len(board), len(board[0])

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if board[i][j] == 'X':
                mine_count += 1

    return mine_count

def reveal_empty_cells(board, revealed, row, col):
    if revealed[row][col]:
        return
    
    revealed[row][col] = True
    if board[row][col] == ' ':
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            reveal_empty_cells(board, revealed, i)

def main():
    rows = 5
    cols = 5
    mines = 5

    board = initialize_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    game_over = False

    while not game_over:
        print_board(revealed)
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))

        if board[row][col] == 'X':
            print('Game Over! You hit a mine.')

        game_over = True
    else:
        mines_around = count_adjacent_mines(board, row, col)
        revealed[row][col] = True

        if mines_around == 0:

            reveal_empty_cells(board, revealed, row, col)

            print_board(board)

        if __name__ == "__main__":
            main
    
                                