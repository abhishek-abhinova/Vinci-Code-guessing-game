import os
import sys
import random

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
colors = ["\033[41m\033[97m", "\033[43m\033[30m", "\033[42m\033[30m", "\033[44m\033[97m", "\033[45m\033[97m"]

for i in range(1, num_players + 1):
    name = input(f"Enter Player {i} Name: ")
    players[i] = {
        'name': name,
        'color': colors[i - 1],
        'lines': set(),
        'triangles': set(),
        'squares': set(),
        'score': 0,
        'hints_used': 0  # Track hints per player
    }

# --- Dice-based Turn Order ---
player_rolls = {}
print("\nRolling 6 dice for each player to determine turn order...")
for pid in players:
    rolls = [random.randint(1, 6) for _ in range(6)]
    total = sum(rolls)
    player_rolls[pid] = total
    print(f"{players[pid]['name']} rolled {rolls} -> Total: {total}")

# Determine turn order
turn_order = sorted(player_rolls, key=lambda x: player_rolls[x], reverse=True)
print("\nTurn order based on dice rolls:")
for i, pid in enumerate(turn_order, start=1):
    print(f"{i}. {players[pid]['name']} (Total: {player_rolls[pid]})")

# --- Board Setup ---
spots = {i: {"R": None, "L": None} for i in range(1, 18)}
move_history = []

# --- Helper Functions ---
def get_display(spot_num, side):
    val = spots[spot_num][side]
    base = f"{spot_num:1}"
    if val is None:
        return f"\033[1;97m {base} \033[0m"
    else:
        color = players[val]['color']
        return f"\033[1;107m{color} {base} \033[0m"

def draw_custom_board():
    def cell(c):
        return f"\033[1;97m {c}\033[0m"
    print("\n          ╔════╦════╦════╗")
    print(f"          ║{cell(get_display(7,'R'))}║{cell(get_display(6,'R'))}║{cell(get_display(5,'R'))}║  R")
    print("          ║════╬════╣════╣")
    print(f"          ║{cell(get_display(8,'R'))}║{cell(get_display(1,'R'))}║{cell(get_display(4,'R'))}║")
    print("╔════╦════╬════╬════╬════╣")
    print(f"║{cell(get_display(3,'L'))}║{cell(get_display(2,'L'))}║{cell(get_display(9,'R'))}║{cell(get_display(2,'R'))}║{cell(get_display(3,'R'))}║")
    print("╠════╬════╬════╬════╩════╝")
    print(f"║{cell(get_display(4,'L'))}║{cell(get_display(1,'L'))}║{cell(get_display(8,'L'))}║          ")
    print("╠════╬════╬════╣           ")
    print(f"║{cell(get_display(5,'L'))}║{cell(get_display(6,'L'))}║{cell(get_display(7,'L'))}║            L")
    print("╚════╩════╩════╝          \n")

def draw_score_board():
    print("\nCurrent Scores:")
    for pid in players:
        score = players[pid]['score']
        print(f"{players[pid]['color']}  {players[pid]['name'].upper()} (P{pid}) -> {score} pts \033[0m")

def count_player_spots():
    counts = {pid: 0 for pid in players}
    for spot in spots.values():
        for side in ['R', 'L']:
            if spot[side] in counts:
                counts[spot[side]] += 1
    return counts

def check_turn(turn):
    index = turn % num_players
    return turn_order[index]

# Spot 9 rules
def valid_spot_9(player_num):
    original = spots[9].copy()
    spots[9]["R"] = player_num  # simulate placing
    lines = [
        [(1, 'R'), (5, 'R'), (9, 'R')],
        [(5, 'L'), (1, 'L'), (9, 'R')],
        [(7, 'R'), (8, 'R'), (9, 'R')],
        [(3, 'R'), (2, 'R'), (9, 'R')],
        [(1, 'L'), (9, 'R'), (1, 'R')],
        [(3, 'L'), (2, 'L'), (9, 'R')],
        [(7, 'L'), (8, 'L'), (9, 'R')],
        [(8, 'R'), (9, 'R'), (8, 'L')],
        [(2, 'L'), (9, 'R'), (2, 'R')]
    ]
    valid = any(all(spots[spot][side] == player_num for (spot, side) in line) for line in lines)
    spots[9] = original
    return valid

def update_score(player_num):
    points = 0
    # Lines, triangles, squares (same as your original code)
    # ... [Copy your previous lines, triangles, squares lists and scoring logic here] ...
    # Example for lines:
    lines = [
        [(1, 'R'), (5, 'R'), (9, 'R')],
        [(5, 'L'), (1, 'L'), (9, 'L')],
        [(7, 'R'), (8, 'R'), (9, 'R')],
        # add all other line patterns...
    ]
    for line in lines:
        if all(spots[spot][side] == player_num for (spot,side)  in line):
            points += 3
    # Triangles and squares similarly
    players[player_num]['score'] = points

def get_hint(player_num):
    for spot in range(1, 10):
        for side in ['R', 'L']:
            if spots.get(spot) and spots[spot][side] is None:
                print(f"Hint: Try spot {spot} side {side}")
                return
    print("No available moves for hint.")

# --- Main Game Loop ---
turn = 0
playing = True

while playing:
    if turn == 17:
        playing = False
        break

    draw_custom_board()
    draw_score_board()

    current_player = check_turn(turn)
    print(f"\nIt's {players[current_player]['name']}'s turn!")

    # If it's the last turn and Spot 9 is completely empty, auto-assign it
    if turn == 16:
        if spots[9]["R"] is None and spots[9]["L"] is None:
            print(f"\nAuto-assigning Spot 9 to {players[current_player]['name']} (last turn).")
            spots[9]["R"] = current_player
            spots[9]["L"] = current_player
            move_history.append((9, "R"))
            move_history.append((9, "L"))
            update_score(current_player)
            turn += 1
            input("Spot 9 assigned. Press Enter to continue...")
            continue

    # Spot 9 claim prompt
    if spots[9]["R"] is None and spots[9]["L"] is None:
        try_spot9 = input("Do you want to claim Spot 9? (y/n): ").strip().lower()
        if try_spot9 is None or try_spot9 == '':
            # Auto-move: pick first available side
            for side_9 in ['R', 'L']:
                if spots[9][side_9] is None:
                    spots[9][side_9] = current_player
                    move_history.append((9, side_9))
                    update_score(current_player)
                    turn += 1
                    print(f" Spot 9 side {side_9} taken.")
                    input("Press Enter to continue...")
                    break
            continue
        if try_spot9 == 'y':
            if not valid_spot_9(current_player):
                print("You must form a line of 3 to claim Spot 9.")
                beep()
                input("Press Enter to continue...")
                continue
            side_9 = input("Enter side for Spot 9 (Enter R for claiming spot 9): ").strip().upper()
            if side_9 is None or side_9 == '':
                for s in ['R', 'L']:
                    if spots[9][s] is None:
                        side_9 = s
                        break
            if side_9 not in ['R', 'L']:
                print("Invalid side.")
                beep()
                input("Press Enter to continue...")
                continue
            spots[9][side_9] = current_player
            move_history.append((9, side_9))
            update_score(current_player)
            turn += 1
            input("Spot 9 claimed. Press Enter to continue...")
            continue
        elif try_spot9 == 'n':
            print("You chose not to claim Spot 9.")
            side = input("Enter side (R for right, or L for left): ").strip().upper()
            if side not in ['R', 'L']:
                print("Invalid side.")
                beep()
                input("Press Enter to continue...")
                continue
            spot_input = input("Enter spot number (1-8) or 'b' to back: ")

            # New feature: show available spots for the player
            available_spots = [s for s in range(1, 9) if spots[s][side] is None]
            if available_spots:
                print(f"Available spots on {side} for you: {available_spots}")
            else:
                print(f"No available spots on {side} for you.")

            if spot_input.lower() == 'b':
                if move_history:
                    last_spot, last_side = move_history.pop()
                    spots[last_spot][last_side] = None
                    turn -= 1
                    print("Last move undone.")
                else:
                    print("Nothing to undo.")
                    beep()
                input("Press Enter to continue...")
                continue
            elif spot_input.isdigit():
                spot = int(spot_input)
                if spot not in range(1, 9):
                    print("Invalid spot.")
                    input("Press Enter to continue...")
                    continue
                if spots[spot][side] is not None:
                    print("That side of the spot is already taken.")
                    beep()
                    input("Press Enter to continue...")
                    continue
                spots[spot][side] = current_player
                move_history.append((spot, side))
                update_score(current_player)
                turn += 1  # Advance turn only after a successful move
                input("Move recorded. Press Enter to continue...")
                continue
            else:
                print("Invalid input.")
                beep()
                input("Press Enter to continue...")
                continue
    else:
        # Spot 9 is partially or fully occupied, skip prompt and go to regular spot logic
        pass

    # Regular spot logic (for both branches above)
    side = input("Enter side (R for right, or L for left): ").strip().upper()
    if side is None or side == '':
        print("No input provided.")
        beep()
        input("Press Enter to continue...")
        continue
    elif side not in ['R', 'L']:
        print("Invalid side.")
        beep()
        input("Press Enter to continue...")
        continue
    else:
        spot_input = input("Enter spot number (1-8) or 'b' to back: ").strip()
        if spot_input is None or spot_input == '':
            print("No input provided.")
            beep()
            input("Press Enter to continue...")
            continue
        elif spot_input.lower() == 'b':
            if move_history:
                last_spot, last_side = move_history.pop()
                spots[last_spot][last_side] = None
                turn -= 1
                print("Last move undone.")
            else:
                print("Nothing to undo.")
                beep()
            input("Press Enter to continue...")
            continue
        elif spot_input.isdigit():
            spot = int(spot_input)
            if spot not in range(1, 9):
                print("Invalid spot.")
                beep()
                input("Press Enter to continue...")
                continue
            if spots[spot][side] is not None:
                print("That side of the spot is already taken.")
                beep()
                input("Press Enter to continue...")
                continue
            available_spots = [s for s in range(1, 9) if spots[s][side] is None]
            if available_spots:
                print(f"Available spots on {side} for you: {available_spots}")
            else:
                print(f"No available spots on {side} for you.")
            spots[spot][side] = current_player
            move_history.append((spot, side))
            print(f"Spot {spot} side {side} taken by {players[current_player]['name']}.")
            # Update score after a successful move
            update_score(current_player)
            turn += 1  # Advance turn only after a successful move
            input("Move recorded. Press Enter to continue...")
            continue
        else:
            print("Invalid input.")
            beep()
            input("Press Enter to continue...")
            continue
    
playing = False  # Added to exit the loop after one complete turn

# Now, after the loop, handle the final balance phase
if turn == 17:
    draw_custom_board()
    print("\n--- FINAL BALANCE PHASE ---\n")
    spot_counts = count_player_spots()
    max_spots = max(spot_counts.values())
    min_spots = min(spot_counts.values())

    if max_spots == min_spots:
        print("All players already have equal spots.")
    else:
        protected = {}
        # 2 Players
        if num_players == 2:
            p1 = 1
            p2 = 2
            # Player 1 protects a spot
            owned = [(i, side) for i in range(1, 18) for side in ['R', 'L'] if spots[i][side] == p1]
            print(f"{players[p1]['name']}, your spots: {owned}")
            while True:
                try:
                    prot_spot = int(input(f"{players[p1]['name']}, enter spot number to protect: "))
                    prot_side = input("Enter side to protect (R/L): ").strip().upper()
                    if (prot_spot, prot_side) in owned:
                        protected[p1] = (prot_spot, prot_side)
                        print(f"{players[p1]['name']} protects spot {prot_spot} side {prot_side}.")
                        break
                    else:
                        print("Invalid choice. Try again.")
                except Exception:
                    print("Invalid input. Try again.")

            # Player 2 removes one of Player 1's spots (not protected)
            removable = [(i, side) for (i, side) in owned if (i, side) != protected[p1]]
            print(f"{players[p2]['name']}, you can remove one of {players[p1]['name']}'s spots (not protected): {removable}")
            while True:
                try:
                    rem_spot = int(input(f"{players[p2]['name']}, enter spot number to remove: "))
                    rem_side = input("Enter side to remove (R/L): ").strip().upper()
                    if (rem_spot, rem_side) in removable:
                        spots[rem_spot][rem_side] = None
                        print(f"{players[p2]['name']} removes {players[p1]['name']}'s spot {rem_spot}-{rem_side}")
                        break
                    else:
                        print("Invalid choice. Try again.")
                except Exception:
                    print("Invalid input. Try again.")

        # 3 Players
        elif num_players == 3:
            for p in [1, 2]:
                for i in range(1, 18):
                    for side in ['R', 'L']:
                        if spots[i][side] == p:
                            protected[p] = (i, side)
                            print(f"{players[p]['name']} protects spot {i} side {side}.")
                            break
                if p in protected:
                    break
            for target in [1, 2]:
                for i in range(1, 18):
                    for side in ['R', 'L']:
                        if (i, side) != protected[target] and spots[i][side] == target:
                            spots[i][side] = None
                            print(f"{players[3]['name']} removes {players[target]['name']}'s spot {i}-{side}")
                            break
                else:
                    continue
                break

        # 4 Players
        elif num_players == 4:
            p1 = 1
            p2 = 2
            for i in range(1, 18):
                for side in ['R', 'L']:
                    if spots[i][side] == p1:
                        protected[p1] = (i, side)
                        print(f"{players[p1]['name']} protects spot {i} side {side}.")
                        break
            for i in range(1, 18):
                for side in ['R', 'L']:
                    if (i, side) != protected[p1] and spots[i][side] == p1:
                        spots[i][side] = None
                        print(f"{players[p2]['name']} removes {players[p1]['name']}'s spot {i}-{side}")
                        break
                else:
                    continue
                break

        # 5 Players
        elif num_players == 5:
            for p in [1, 2]:
                for i in range(1, 18):
                    for side in ['R', 'L']:
                        if spots[i][side] == p:
                            protected[p] = (i, side)
                            print(f"{players[p]['name']} protects spot {i} side {side}.")
                            break
                    if p in protected:
                        break
            for i in range(1, 18):
                for side in ['R', 'L']:
                    if (i, side) != protected[1] and spots[i][side] == 1:
                        spots[i][side] = None
                        print(f"{players[3]['name']} removes {players[1]['name']}'s spot {i}-{side}")
                        break
                else:
                    continue
                break
            for i in range(1, 18):
                for side in ['R', 'L']:
                    if (i, side) != protected[2] and spots[i][side] == 2:
                        spots[i][side] = None
                        print(f"{players[4]['name']} removes {players[2]['name']}'s spot {i}-{side}")
                        break
                else:
                    continue
                break

    # --- RECALCULATE SCORES FOR ALL PLAYERS ---
    for pid in players:
        update_score(pid)
    draw_custom_board()
    print("\n--- FINAL BALANCE PHASE COMPLETE ---")
    print("\n--- FINAL SCORES ---")
    print("\nGame Over! Calculating final scores...\n")
    draw_score_board()
    # --- WINNER DECLARATION ---
    print("\nCalculating winner...\n")
    beep()
    scores = {pid: players[pid]['score'] for pid in players}
    max_score = max(scores.values())
    winners = [pid for pid, s in scores.items() if s == max_score]

    if len(winners) == 1:
        winner = winners[0]
        print(f"\n🏆 Winner is {players[winner]['name']} with {max_score} points!")
    else:
        print("\n🤝 It's a tie between:")
        for pid in winners:
            print(f" - {players[pid]['name']}")

    input("\nPress Enter to return to the main menu or close the window.")
