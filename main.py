def display_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)


# Функция для проверки выигрышных комбинаций
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False


# Главная функция игры
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    winner = None
    moves = 0

    while not winner and moves < 9:
        display_board(board)
        col = int(input(f"Игрок {players[current_player]}, Введи колонну (0-2): "))
        row = int(input(f"Игрок {players[current_player]}, Введи клетку (0-2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = players[current_player]
            moves += 1
            if check_win(board, players[current_player]):
                winner = players[current_player]
            current_player = (current_player + 1) % 2
        else:
            print("Неправильный ход, попробуй еще раз")

    display_board(board)

    if winner:
        print(f"Игрок {winner} Победил!")
    else:
        print("Ничья!")


# Запуск игры
tic_tac_toe()
