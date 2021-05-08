xx_num = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
win = 0

theBoard = {
    "u1": " ",
    "u2": " ",
    "u3": " ",
    "m1": " ",
    "m2": " ",
    "m3": " ",
    "l1": " ",
    "l2": " ",
    "l3": " "
}


def printBoard(board_values):
    UL = board_values["l1"];
    UM = board_values["l2"];
    UR = board_values["l3"];
    ML = board_values["m1"];
    MM = board_values["m2"];
    MR = board_values["m3"];
    DL = board_values["u1"];
    DM = board_values["u2"];
    DR = board_values["u3"];

    onScreen = f"""                    			        
						MAP									
	      |    |                         1 | 2 | 3
	   {UL}  | {UM}  | {UR}            	    ___|___|___ 				 
	 _____|____|_____                    4 | 5 | 6
	      |    |                        ___|___|___
	   {ML}  | {MM}  | {MR}                       7 | 8 | 9
	 _____|____|_____                
	      |	   |                       
	   {DL}  | {DM}  | {DR}            
	      |	   |	                    

	"""
    print(onScreen)


def taker0X():
    xx = input("option 0 or X => ")
    if xx not in ["X", "0", "x", "o", 0]:
        taker0X()

    if xx == "x":
        xx = "X"
        return xx
    if xx == 0:
        xx = "0"
        return xx
    if xx == "o":
        xx = "0"
        return xx

    xx = "X"
    return xx


def winChecker(win=0):
    if theBoard["u1"] == theBoard["u2"] and theBoard["u2"] == theBoard["u3"]:
        win = 5
        if theBoard["u1"] == ' ':
            win = 10

    if theBoard["m1"] == theBoard["m2"] and theBoard["m2"] == theBoard["m3"]:
        win = 5
        if theBoard["m1"] == ' ':
            win = 10

    if theBoard["l1"] == theBoard["l2"] and theBoard["l2"] == theBoard["l3"]:
        win = 5
        if theBoard["l1"] == ' ':
            win = 10

    if theBoard["u1"] == theBoard["m1"] and theBoard["m1"] == theBoard["l1"]:
        win = 5
        if theBoard["u1"] == ' ':
            win = 10

    if theBoard["u2"] == theBoard["m2"] and theBoard["m2"] == theBoard["l2"]:
        win = 5
        if theBoard["u2"] == ' ':
            win = 10

    if theBoard["u3"] == theBoard["m3"] and theBoard["m3"] == theBoard["l3"]:
        win = 5
        if theBoard["u3"] == ' ':
            win = 10

    if theBoard["u1"] == theBoard["m2"] and theBoard["m2"] == theBoard["l3"]:
        win = 5
        if theBoard["u1"] == ' ':
            win = 10

    if theBoard["u3"] == theBoard["m2"] and theBoard["m2"] == theBoard["l1"]:
        win = 5
        if theBoard["u3"] == ' ':
            win = 10

    return win


def drawChecker(draw=0):
    for item in theBoard.values():
        if item == " ":
            draw += 1
    return draw


class userNames:
    username1 = input("enter username for player1 ")
    if len(username1) == 0:
        username1 = "user1"
    userOption_1 = taker0X()

    username2 = input("enter username for player2 ")
    if len(username2) == 0:
        username2 = "user2"
    if userOption_1 == "0":
        userOption_2 = "X"
    if userOption_1 == "X":
        userOption_2 = "0"


def optionDisplayer():
    print(f"""
		%10s VS %-2s
		%8s     %4s
	      """ % (userNames.username1, userNames.username2, userNames.userOption_1, userNames.userOption_2))


def intConverter(num):
    nmLst = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    if num not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        for xx_num in nmLst.keys():
            if num == xx_num:
                num = nmLst[xx_num]
                return num


def takerOption(player):
    i = input(f"Avilable options for {player}, {list(xx_num.values())}=> ")
    i = intConverter(i)
    while i not in xx_num.values():
        i = input(f"Avilable options for {player}, {list(xx_num.values())}=> ")
        i = intConverter(i)

    temp = str(i)
    del xx_num[temp]
    return i


def fill0X(taker, userOptions):
    if taker == "1" or taker == 1:
        theBoard["l1"] = userOptions
    if taker == "2" or taker == 2:
        theBoard["l2"] = userOptions
    if taker == "3" or taker == 3:
        theBoard["l3"] = userOptions
    if taker == "4" or taker == 4:
        theBoard["m1"] = userOptions
    if taker == "5" or taker == 5:
        theBoard["m2"] = userOptions
    if taker == "6" or taker == 6:
        theBoard["m3"] = userOptions
    if taker == "7" or taker == 7:
        theBoard["u1"] = userOptions
    if taker == "8" or taker == 8:
        theBoard["u2"] = userOptions
    if taker == "9" or taker == 9:
        theBoard["u3"] = userOptions


def playing():
    for i in range(9):
        playtime = 1
        print("\n")

        if playtime == 1:
            optionDisplayer()

            printBoard(theBoard)
            print(f"\t\t {userNames.username1} turn ({userNames.userOption_1})\n")
            take = takerOption(userNames.username1)

            fill0X(take, userNames.userOption_1)

            draw = drawChecker()
            if draw == 0:
                print("\n\n\t\tMATCH DRAW\n\n")
                break

            winner = winChecker()
            if winner == 5:
                printBoard(theBoard)
                print(f"\t{userNames.username1} is a winner\n\n")
                break
            playtime += 1

        if playtime == 2:
            optionDisplayer()

            printBoard(theBoard)
            print(f"\t\t {userNames.username2} turn ({userNames.userOption_2})\n")
            take = takerOption(userNames.username2)

            fill0X(take, userNames.userOption_2)

            draw = drawChecker()
            if draw == 0:
                print("\nMATCH DRAW\n")
                break

            winner = winChecker()
            if winner == 5:
                printBoard(theBoard)
                print(f"\t{userNames.username2} is a winner\n\n")
                break
            playtime -= 1


def playTimes(play):
    i = 0
    while i < 1:
        play
        ask = input("\nPlay(p) to play again\nExit(e) to exit the game => ")

        if ask == "p" or ask == "play" or ask == "Play" or ask == "PLAY" or ask == "P":
            play

        if ask == "e" or ask == "exit" or ask == "Exit" or ask == "EXIT" or ask == "E":
            i += 1
    print("\n\nthank for playing")


playTimes(playing())
