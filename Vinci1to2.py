import os
a=input("Enter 1st Player Name P1 : ")
b=input("Enter 2nd Player Name P2 : ")
spots = {1 : "1 ", 2 : "2 ", 3 : "3 ", 4 : "4 ", 5 : "5 ", 6 : "6 ", 7 : "7 ", 8 : "8 ", 9 : "9 ", 10 : "10", 11 : "11", 12 : "12", 13 : "13", 14 : "14", 15 : "15", 16 : "16", 17 : "17"}
def draw_board(spots):
    board2 = (f"|----|----|₁ {spots[1]}|₂ {spots[2]}|₃ {spots[3]}|\n"
                f"|----|----|₄ {spots[4]}|₅ {spots[5]}|₆ {spots[6]}|\n"
                f"|₇ {spots[7]}|₈ {spots[8]}|₉ {spots[9]}|₁₀{spots[10]}|₁₁{spots[11]}|\n"
                f"|₁₂{spots[12]}|₁₃{spots[13]}|₁₄{spots[14]}|----|----|\n"
                f"|₁₅{spots[15]}|₁₆{spots[16]}|₁₇{spots[17]}|----|----|")
    print(board2)
playing = True
turn = 0
prev_turn = -1
def check_turn(turn):
    if turn % 2 == 0:
        return f"\033[94m{"P2"}\033[0m"
    elif turn % 2 != 0:
        return f"\033[91m{"P1"}\033[0m"
pointsP1 = 0
pointsP2 = 0
def TallyPoints1(pointsP1):
    #Horozontial 3
    if (spots[1] == spots[2] == spots[3] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[4] == spots[5] == spots[6] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[7] == spots[8] == spots[9] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[8] == spots[9] == spots[10] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[9] == spots[10] == spots[11] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[14] == spots[13] == spots[12] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[17] == spots[16] == spots[15] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    #Vertical 3
    if (spots[3] == spots[6] == spots[11] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[2] == spots[5] == spots[10] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[1] == spots[4] == spots[9] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[4] == spots[9] == spots[14] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[9] == spots[14] == spots[17] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[8] == spots[13] == spots[16] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[7] == spots[12] == spots[15] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    #Diagonal 3
    if (spots[1] == spots[5] == spots[11] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[3] == spots[5] == spots[9] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[5] == spots[9] == spots[13] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[9] == spots[13] == spots[15] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    if (spots[17] == spots[13] == spots[7] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 3
    #Triangles in TOP
    #125 214 145 254 652 325 236 365 549 894 (4,9,10) (4,5,10) (5,10,9) (5,10,11) (6,5,10) (5,6,11) (6,10,11) 
    if (spots[1] == spots[2] == spots[4] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[2] == spots[1] == spots[4] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[1] == spots[4] == spots[5] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[2] == spots[5] == spots[4] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[6] == spots[5] == spots[2] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[3] == spots[2] == spots[5] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[2] == spots[3] == spots[6] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[3] == spots[6] == spots[5] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[5] == spots[4] == spots[9] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[8] == spots[4] == spots[9] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[4] == spots[9] == spots[10] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[4] == spots[5] == spots[10] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[5] == spots[10] == spots[9] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[5] == spots[10] == spots[11] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[6] == spots[5] == spots[10] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[5] == spots[6] == spots[11] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[6] == spots[10] == spots[11] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    # Triangles in Bottom
    #(8,7,12) (7,12,13) (8,13,12) (8,13,14) (8,9,13) (8,9,14) (9,14,13) (14,9,10) (12,15,16) (13,12,15) (12,13,16) (13,16,15) (13,16,17) (14,13,16) (13,14,17) (14,17,16) (10,9,14)
    if (spots[8] == spots[7] == spots[2] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[7] == spots[12] == spots[13] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[8] == spots[13] == spots[12] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[13] == spots[8] == spots[14] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[13] == spots[9] == spots[8] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[14] == spots[9] == spots[8] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[9] == spots[14] == spots[13] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[14] == spots[9] == spots[10] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[12] == spots[15] == spots[16] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[13] == spots[12] == spots[15] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[12] == spots[13] == spots[16] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[13] == spots[16] == spots[15] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[13] == spots[16] == spots[17] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[14] == spots[13] == spots[16] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[13] == spots[14] == spots[17] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[14] == spots[17] == spots[16] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    if (spots[10] == spots[4] == spots[9] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 += 1
    #square in Top
    if (spots[1] == spots[2] == spots[4] == spots[5] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    if (spots[3] == spots[2] == spots[6] == spots[5] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    if (spots[4] == spots[9] == spots[5] == spots[10] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    if (spots[5] == spots[10] == spots[6] == spots[11] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    #square in Bottom
    if (spots[7] == spots[8] == spots[12] == spots[13] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    if (spots[8] == spots[13] == spots[9] == spots[4] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    if (spots[12] == spots[13] == spots[15] == spots[16] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    if (spots[13] == spots[16] == spots[17] == spots[14] == f"\033[91m{"P1"}\033[0m"):
        pointsP1 -= 2
    print(a+" (P1) : " + str(pointsP1) + " Points")

def TallyPoints2(pointsP2):
    #Horozontial 3
    if (spots[1] == spots[2] == spots[3] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[4] == spots[5] == spots[6] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[7] == spots[8] == spots[9] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[8] == spots[9] == spots[10] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[9] == spots[10] == spots[11] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[14] == spots[13] == spots[12] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[17] == spots[16] == spots[15] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    #Vertical 3
    if (spots[3] == spots[6] == spots[11] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[2] == spots[5] == spots[10] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[1] == spots[4] == spots[9] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[4] == spots[9] == spots[14] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[9] == spots[14] == spots[17] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[8] == spots[13] == spots[16] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[7] == spots[12] == spots[15] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    #Diagonal 3
    if (spots[1] == spots[5] == spots[11] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[3] == spots[5] == spots[9] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[5] == spots[9] == spots[13] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[9] == spots[13] == spots[15] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    if (spots[17] == spots[13] == spots[7] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 3
    #Triangles in TOP
    #125 214 145 254 652 325 236 365 549 894 (4,9,10) (4,5,10) (5,10,9) (5,10,11) (6,5,10) (5,6,11) (6,10,11) 
    if (spots[1] == spots[2] == spots[4] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[2] == spots[1] == spots[4] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[1] == spots[4] == spots[5] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[2] == spots[5] == spots[4] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[6] == spots[5] == spots[2] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[3] == spots[2] == spots[5] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[2] == spots[3] == spots[6] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[3] == spots[6] == spots[5] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[5] == spots[4] == spots[9] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[8] == spots[4] == spots[9] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[4] == spots[9] == spots[10] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[4] == spots[5] == spots[10] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[5] == spots[10] == spots[9] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[5] == spots[10] == spots[11] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[6] == spots[5] == spots[10] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[5] == spots[6] == spots[11] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[6] == spots[10] == spots[11] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    # Triangles in Bottom
    #(8,7,12) (7,12,13) (8,13,12) (8,13,14) (8,9,13) (8,9,14) (9,14,13) (14,9,10) (12,15,16) (13,12,15) (12,13,16) (13,16,15) (13,16,17) (14,13,16) (13,14,17) (14,17,16) (10,9,14)
    if (spots[8] == spots[7] == spots[2] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[7] == spots[12] == spots[13] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[8] == spots[13] == spots[12] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[13] == spots[8] == spots[14] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[13] == spots[9] == spots[8] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[14] == spots[9] == spots[8] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[9] == spots[14] == spots[13] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[14] == spots[9] == spots[10] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[12] == spots[15] == spots[16] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[13] == spots[12] == spots[15] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[12] == spots[13] == spots[16] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[13] == spots[16] == spots[15] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[13] == spots[16] == spots[17] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[14] == spots[13] == spots[16] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[13] == spots[14] == spots[17] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[14] == spots[17] == spots[16] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
    if (spots[10] == spots[4] == spots[9] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 += 1
     #square in Top
    if (spots[1] == spots[2] == spots[4] == spots[5] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    if (spots[3] == spots[2] == spots[6] == spots[5] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    if (spots[4] == spots[9] == spots[5] == spots[10] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    if (spots[5] == spots[10] == spots[6] == spots[11] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    #square in Bottom
    if (spots[7] == spots[8] == spots[12] == spots[13] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    if (spots[8] == spots[13] == spots[9] == spots[4] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    if (spots[12] == spots[13] == spots[15] == spots[16] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    if (spots[13] == spots[16] == spots[17] == spots[14] == f"\033[94m{"P2"}\033[0m"):
        pointsP2 -= 2
    print(b+" (P2) : "+ str(pointsP2) + " Points")

while playing:
    # clear console
    os.system('cls' if os.name == 'nt' else 'clear')
    # draw board
    draw_board(spots)

    #end of game
    if turn == 17:
        playing = False
        print(a," P1 , pick a spot to protect")
        protected_spot = input()
        print(int(protected_spot))
        if spots[int(protected_spot)] == f"\033[94m{"P2"}\033[0m":
            while spots[int(protected_spot)] == f"\033[94m{"P2"}\033[0m":
                print(b" P2 , pick a different spot")
                protected_spot = input()

        print(b," P2 , pick a spot to remove other than the protected one")
        removed_spot = input()

        if int(protected_spot) == int(removed_spot) or spots[int(removed_spot)] == f"\033[94m{"P2"}\033[0m":
            while protected_spot == removed_spot or spots[int(removed_spot)] == f"\033[94m{"P2"}\033[0m":
                print(b," P2 , pick a different spot")
                removed_spot = input()

        spots[int(removed_spot)] = "--"
        draw_board(spots)
        TallyPoints1(pointsP1)
        TallyPoints2(pointsP2)
        if pointsP1 > pointsP2: print(a," wins!")
        if pointsP1 < pointsP2: print(b," wins!")
        elif pointsP1 == pointsP2: print("Tie!")


    #invalid turn
    if prev_turn == turn and int(turn) < 17:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    if turn%2==0:
        print(a+" P" + str((turn % 2) + 1) + "'s turn: Pick your spot or press s to check score")
    else:
        print(b+" P" + str((turn % 2) + 1) + "'s turn: Pick your spot or press s to check score")
    choice = input()

    # score check
    if choice == 's':
        while choice == 's':
            TallyPoints1(pointsP1)
            TallyPoints2(pointsP2)
            print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot or press s to check score")
            choice = input()
            #playing = False

    elif str.isdigit(choice) and int(choice) in spots and int(turn) < 17:
        # occupancy test.
        if not spots[int(choice)] in {f"\033[94m{"P2"}\033[0m", f"\033[91m{"P1"}\033[0m"}:
            # update turn and mark down spot
            turn += 1
            spots[int(choice)] = check_turn(turn)


