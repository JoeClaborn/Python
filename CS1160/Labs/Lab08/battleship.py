# Joe Claborn - CS1160 - Lab 08

def create_board():
    return [[' ' for _ in range(10)] for _ in range(10)]

def print_board(board, reveal=False):
    print("  " + " ".join(str(i+1) for i in range(10)))
    for i, row in enumerate(board):
        print(str(i+1) + " " + " ".join(cell if reveal or cell in ('X', 'O') else ' ' for cell in row))

def place_ships():
    board = create_board()
    ships = {
        'A': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],  # 5-unit ship
        'B': [(2, 2), (2, 3), (2, 4), (2, 5)],  # 4-unit ship
        'C': [(4, 5), (5, 5), (6, 5)],  # 3-unit ship
        'D': [(7, 1), (7, 2)],  # 2-unit ship
        'E': [(9, 7), (9, 8)],  # 2-unit ship
        'F': [(5, 0)],  # 1-unit ship
        'G': [(8, 9)]  # 1-unit ship
    }
    for symbol, positions in ships.items():
        for row, col in positions:
            board[row][col] = symbol
    return board

def all_ships_sunk(board):
    return all(cell in (' ', 'X', 'O') for row in board for cell in row)

def player_turn(name, board, attack_board):
    print(f"{name}'s turn!\n{name}'s Previous Guesses:")
    print_board(attack_board)
    while True:
        try:
            row = int(input("Guess a Row: ")) - 1
            col = int(input("Guess a Column: ")) - 1
            if 0 <= row < 10 and 0 <= col < 10 and attack_board[row][col] == ' ':
                break
            print("You already guessed that coordinate!")
        except ValueError:
            print("Your input was not in the range of the grid!")
    
    if board[row][col] != ' ':
        print("Good Shot! You hit your opponent's battleship!")
        attack_board[row][col] = 'X'
        board[row][col] = 'X'
    else:
        print("You missed your opponent's battleship!")
        attack_board[row][col] = 'O'

def main():
    print("Welcome to Battleship!")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    
    board1, board2 = place_ships(), place_ships()
    attack_board1, attack_board2 = create_board(), create_board()
    
    turn = 0
    while True:
        if turn % 2 == 0:
            player_turn(player1, board2, attack_board1)
            if all_ships_sunk(board2):
                print(f"{player1} Wins!")
                break
        else:
            player_turn(player2, board1, attack_board2)
            if all_ships_sunk(board1):
                print(f"{player2} Wins!")
                break
        turn += 1

if __name__ == "__main__":
    main()
