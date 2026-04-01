import os
import sys
def beep():
    sys.stdout.write('\a')
    sys.stdout.flush()
# Setup number of players
num_players = int(input("Enter number of players (2 to 5): "))
while num_players < 2 or num_players > 5:
    print("Invalid input. Please enter a number between 2 and 5.")
    beep()
    num_players = int(input("Enter number of players (2 to 5): "))

players = {}
colors = ["\033[91m", "\033[93m", "\033[92m", "\033[94m", "\033[95m"]  # red, blue, green, purple, yellow

for i in range(1, num_players + 1):
    name = input(f"Enter Player {i} Name: ")
    players[i] = {'name': name, 'symbol': f"{colors[i - 1]}P{i}\033[0m", 'points': 0}

spots = {i: "  " for i in range(1, 18)}
move_history = []


def show_scoreboard(players):
    print("\nScoreboard:") 
    print("──────────────")
    for i in range(1, len(players) + 1):
        tally_points(i) 
        symbol = players[i]['symbol']
        points = players[i]['points']
        name = players[i]['name']
        print(f"{symbol} {name}: {points} points")
    print("──────────────\n")
    
def draw_board(spots):
    board = (
        f"|-----|-----|₁  {spots[1]}|₂  {spots[2]}|₃  {spots[3]}|\n"
        f"|-----|-----|₄  {spots[4]}|₅  {spots[5]}|₆  {spots[6]}|\n"
        f"|₇  {spots[7]}|₈  {spots[8]}|₉  {spots[9]}|₁₀ {spots[10]}|₁₁ {spots[11]}|\n"
        f"|₁₂ {spots[12]}|₁₃ {spots[13]}|₁₄ {spots[14]}|-----|-----|\n"
        f"|₁₅ {spots[15]}|₁₆ {spots[16]}|₁₇ {spots[17]}|-----|-----|"
    )
    print(board)
def check_turn(turn):
    player_num = (turn % num_players) + 1
    return players[player_num]['symbol'], player_num

def TallyPoints(player_num):
    symbol = players[player_num]['symbol']
    points = 0
    lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], [12, 13, 14], [15, 16, 17],
        [1, 5, 11], [2, 5, 10], [3, 6, 11], [7, 12, 15], [8, 13, 16], [9, 14, 17],
        [1, 4, 9], [3, 5, 9], [7, 13, 17], [9, 13, 15], [8, 9, 10], [9, 10, 11], [4, 9, 14], [5, 9, 13]
    ]
    triangles = [
        [1, 2, 5], [2, 1, 4], [1, 4, 5], [2, 5, 4], [6, 5, 2], [3, 2, 5], [2, 3, 6], [3, 6, 5],
        [5, 4, 9], [8, 9, 4], [4, 9, 10], [4, 5, 10], [5, 10, 9], [5, 10, 11], [6, 5, 10], [5, 6, 11], [6, 10, 11],
        [8, 7, 12], [7, 12, 13], [8, 13, 12], [8, 13, 14], [8, 9, 14], [9, 14, 13], [14, 9, 10],
        [12, 15, 16], [7, 8, 13], [13, 12, 15], [12, 13, 16], [13, 16, 15], [13, 16, 17],
        [14, 13, 16], [13, 14, 17], [14, 17, 16], [10, 9, 14], [8, 9, 13]
    ]
    squares = [
        [1, 2, 4, 5], [3, 2, 6, 5], [4, 9, 5, 10], [5, 10, 6, 11],
        [7, 8, 13, 12], [8, 9, 13, 14], [12, 13, 16, 15], [13, 14, 16, 17]
    ]
    for line in lines:
        if all(spots[pos] == symbol for pos in line):
            points += 3
    for triangle in triangles:
        if all(spots[pos] == symbol for pos in triangle):
            points += 1
    for square in squares:
        if all(spots[pos] == symbol for pos in square):
            points -= 2
    players[player_num]['points'] = points

def valid_spot_9(symbol):
    original = spots[9]
    spots[9] = symbol
    lines = [[1, 4, 9], [10, 8, 9], [9, 10, 11], [9, 14, 17], [7, 8, 9], [3, 5, 9], [14, 4, 9], [9, 13, 15], [5, 9, 13]]
    valid = any(all(spots[pos] == symbol for pos in line) for line in lines)
    spots[9] = original
    return valid

# Game loop
turn = 0
playing = True

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # Auto-assign spot 9 on turn 16 if it's still empty
    if turn == 16 and spots[9] == "  ":
        symbol, current_player = check_turn(turn)
        print(f"\nSpot 9 is empty and it's turn 17. Automatically assigning to {players[current_player]['name']}.")
        spots[9] = symbol
        move_history.append(9)
        turn += 1
        input("Press Enter to continue...")
        continue

    print("\nCurrent Scores:")
    for i in range(1, num_players + 1):
        TallyPoints(i)
        print(f"{players[i]['name']} (P{i}): {players[i]['points']} Points")

    if turn == 17:
        print("\nEnd Game Phase Started.")
        move_count = {i: 0 for i in range(1, num_players + 1)}
        for pos in spots:
            for i in range(1, num_players + 1):
                if spots[pos] == players[i]['symbol']:
                    move_count[i] += 1
        max_moves = max(move_count.values())
        top_players = [i for i, count in move_count.items() if count == max_moves]
        protector = top_players[0]
        print(f"{players[protector]['name']} gets to protect one of their spots.")

        while True:
            protected_input = input("Enter spot number to protect: ")
            if protected_input.isdigit():
                protected = int(protected_input)
                if spots[protected] == players[protector]['symbol']:
                    break
                else:
                    print("You can only protect your own spot.")
                    beep()
            else:
                print("Invalid input. Try again.")
                beep()
                continue 

        # Other players remove a spot
        for j in range(1, num_players + 1):
            if j == protector:
                continue
            print(f"{players[j]['name']} may remove a piece.")
            while True:
                remove_input = input("Enter spot number to remove: ")
                if remove_input.isdigit():
                    to_remove = int(remove_input)
                    if to_remove == protected:
                        print("That spot is protected.")
                        beep()
                    elif spots[to_remove] == players[j]['symbol']:
                        print("You can't remove your own spot.")
                        beep()
                    elif spots[to_remove] == "  ":
                        print("Spot is empty.")
                        beep()
                    else:
                        spots[to_remove] = "  "
                        break
                else:
                    print("Invalid input.")
                    beep()
        draw_board(spots)
        print("\nFinal Scores:")
        for i in range(1, num_players + 1):
            TallyPoints(i)
            print(f"{players[i]['name']} (P{i}): {players[i]['points']} Points")
        max_points = max(players[i]['points'] for i in range(1, num_players + 1))
        winners = [players[i]['name'] for i in range(1, num_players + 1) if players[i]['points'] == max_points]
        if len(winners) == 1:
            print(f"🏆 Winner: {winners[0]}!")
        else:
            print("🤝 It's a tie between:", ", ".join(winners))
        break

    symbol, current_player = check_turn(turn)
    print(f"\n{players[current_player]['name']}'s turn (P{current_player}).")
    print("Enter a spot number, 's' to view score, or 'b' to go back:")
    choice = input().strip()
    if choice.lower() == 's':
        continue
    elif choice.lower() == 'b':
        if move_history:
            last_spot = move_history.pop()
            spots[last_spot] = "  "
            turn -= 1
            print("Last move undone.")
        else:
            print("Nothing to undo.")
            beep()
        input("Press Enter to continue...")
        continue
    elif choice.isdigit():
        spot = int(choice)
        if spot not in spots:
            print("Invalid spot. Press Enter.")
            input()
            continue
        if spot == 9 and not valid_spot_9(symbol):
            print("To play on spot 9, you must form a line.")
            beep()
            input("Press Enter to continue...")
            continue
        if spots[spot] == "  ":
            spots[spot] = symbol
            move_history.append(spot)
            turn += 1
        else:
            print("Spot already taken. Press Enter.")
            beep()
            input()
    else:
        print("Invalid input. Press Enter.")
        beep()
        input()