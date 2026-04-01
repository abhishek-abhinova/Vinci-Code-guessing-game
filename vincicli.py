import os
import random

# Setup number of players
num_players = int(input("Enter number of players (1 to 5): "))
while num_players < 1 or num_players > 5:
    print("Invalid input. Please enter a number between 1 and 5.")
    num_players = int(input("Enter number of players (1 to 5): "))

players = {}
colors = ["\033[91m", "\033[94m", "\033[92m", "\033[95m", "\033[93m"]  # red, blue, green, purple, yellow

# If Single Player, assign AI
if num_players == 1:
    player_name = input("Enter your name: ")
    players[1] = {'name': player_name, 'symbol': f"{colors[0]}P1\033[0m", 'points': 0}
    players[2] = {'name': "AI Bot", 'symbol': f"{colors[1]}P2\033[0m", 'points': 0}
    num_players = 2
    ai_player = 2
else:
    for i in range(1, num_players + 1):
        name = input(f"Enter Player {i} Name: ")
        players[i] = {'name': name, 'symbol': f"{colors[i - 1]}P{i}\033[0m", 'points': 0}
    ai_player = None

# Initial spots
spots = {i: " " for i in range(1, 18)}

def draw_board(spots):
    board2 = (
        f"|----|----|₁ {spots[1]}|₂ {spots[2]}|₃ {spots[3]}|\n"
        f"|----|----|₄ {spots[4]}|₅ {spots[5]}|₆ {spots[6]}|\n"
        f"|₇  {spots[7]}|₈  {spots[8]}|₉ {spots[9]}|₁₀{spots[10]}|₁₁{spots[11]}|\n"
        f"|₁₂{spots[12]}|₁₃{spots[13]}|₁₄{spots[14]}|----|----|\n"
        f"|₁₅{spots[15]}|₁₆{spots[16]}|₁₇{spots[17]}|----|----|"
    )
    print(board2)

def check_turn(turn):
    player_num = (turn % num_players) + 1
    return players[player_num]['symbol'], player_num

def TallyPoints(player_num):
    symbol = players[player_num]['symbol']
    points = 0

    lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [12, 13, 14], [15, 16, 17],
        [1, 4, 7], [2, 5, 8], [3, 6, 9], [7, 12, 15], [8, 13, 16], [9, 14, 17],
        [1, 5, 9], [3, 5, 7], [7, 13, 17], [9, 13, 15]
    ]

    squares = [
        [7, 8, 12, 13], [8, 9, 13, 14],
        [12, 13, 15, 16], [13, 14, 16, 17]
    ]

    triangles = [
        [1, 2, 4], [2, 3, 5], [4, 5, 7], [5, 6, 8],
        [7, 8, 12], [8, 9, 13], [12, 13, 15], [13, 14, 16],
        [10, 11, 9], [14, 17, 9]
    ]

    for line in lines:
        if all(spots[pos] == symbol for pos in line):
            points += 3

    for square in squares:
        if all(spots[pos] == symbol for pos in square):
            points += 2

    for triangle in triangles:
        if all(spots[pos] == symbol for pos in triangle):
            points += 1

    players[player_num]['points'] = points

def valid_spot_9(symbol):
    temp_symbol = symbol
    original_value = spots[9]
    spots[9] = temp_symbol

    lines_involving_9 = [
        [7, 8, 9], [3, 6, 9], [1, 5, 9], [9, 13, 17]
    ]

    forms_line = False
    for line in lines_involving_9:
        if all(spots[pos] == temp_symbol for pos in line):
            forms_line = True
            break

    spots[9] = original_value
    return forms_line

def ai_move(ai_symbol, player_symbol):
    possible = [key for key, val in spots.items() if val == " "]

    # AI tries to win
    for move in possible:
        if move == 9 and not valid_spot_9(ai_symbol):
            continue
        spots[move] = ai_symbol
        if any(all(spots[pos] == ai_symbol for pos in line) for line in [
            [1,2,3],[4,5,6],[7,8,9],[12,13,14],[15,16,17],
            [1,4,7],[2,5,8],[3,6,9],[7,12,15],[8,13,16],[9,14,17],
            [1,5,9],[3,5,7],[7,13,17],[9,13,15]
        ]):
            spots[move] = " "
            return move
        spots[move] = " "

    # AI tries to block
    for move in possible:
        if move == 9 and not valid_spot_9(ai_symbol):
            continue
        spots[move] = player_symbol
        if any(all(spots[pos] == player_symbol for pos in line) for line in [
            [1,2,3],[4,5,6],[7,8,9],[12,13,14],[15,16,17],
            [1,4,7],[2,5,8],[3,6,9],[7,12,15],[8,13,16],[9,14,17],
            [1,5,9],[3,5,7],[7,13,17],[9,13,15]
        ]):
            spots[move] = " "
            return move
        spots[move] = " "

    # Center
    if 5 in possible:
        return 5

    # Corners
    corners = [i for i in [1,3,7,9] if i in possible]
    random.shuffle(corners)
    for move in corners:
        if move == 9 and not valid_spot_9(ai_symbol):
            continue
        return move

    # Any
    for move in possible:
        if move == 9 and not valid_spot_9(ai_symbol):
            continue
        return move

playing = True
turn = 0

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if turn == 17:
        playing = False
        print("\nGame End Phase!")
        for i in range(1, num_players + 1):
            TallyPoints(i)
        for i in range(1, num_players + 1):
            print(f"{players[i]['name']} (P{i}): {players[i]['points']} Points")
        max_points = max(players[i]['points'] for i in range(1, num_players + 1))
        winners = [players[i]['name'] for i in range(1, num_players + 1) if players[i]['points'] == max_points]
        if len(winners) == 1:
            print(f"Winner: {winners[0]}!")
        else:
            print("It's a tie between:", ", ".join(winners))
        break

    symbol, current_player = check_turn(turn)
    print(players[current_player]['name'] + f" (P{current_player})'s turn:")

    if ai_player == current_player:
        player_symbol = players[1]['symbol']
        ai_symbol = players[ai_player]['symbol']
        choice = ai_move(ai_symbol, player_symbol)
        print(f"AI picks spot {choice}")
    else:
        print("Pick your spot or press 's' to check score:")
        choice = input()

        if choice == 's':
            for i in range(1, num_players + 1):
                TallyPoints(i)
            for i in range(1, num_players + 1):
                print(f"{players[i]['name']} (P{i}): {players[i]['points']} Points")
            input("Press Enter to continue...")
            continue
        elif choice.isdigit() and int(choice) in spots:
            choice = int(choice)
            if choice == 9 and not valid_spot_9(symbol):
                print("Spot 9 requires forming a line! Press Enter to continue.")
                input()
                continue
        else:
            print("Invalid input. Press Enter to continue.")
            input()
            continue

    if spots[choice] not in [players[i]['symbol'] for i in range(1, num_players + 1)]:
        spots[choice] = symbol
        turn += 1
    else:
        if ai_player == current_player:
            continue
        else:
            print("Spot taken. Press Enter to pick again.")
            input()