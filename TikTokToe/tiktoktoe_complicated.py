import random


class Options:

    board_option_stat= {
            "x1": " ",
            "x2": " ",
            "x3": " ",
            "x4": " ",
            "x5": " ",
            "x6": " ",
            "x7": " ",
            "x8": " ",
            "x9": " ",
            }
    avilable_options_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @classmethod
    def option_avilable(cls, option):
        return option in cls.board_option_stat.values()

    @classmethod
    def option_used(cls, option):
        return option not in cls.board_option_stat.values()

    @classmethod
    def update_option(cls, option, value):
        cls.board_option_stat[option] = value

    @classmethod
    def ask_options(cls):
        return cls.avilable_options_data



#data to be asked from users
class UserInfo():

    def user_info(self):
        print("leave Blank everytime For default select\n")
        user1_name = input("Enter player1 Name: ")

        user1_sign = input("select X or 0: ")

        if str(user1_sign.upper()) not in ["X", "0", "O"]:
            _ = 1
            while _:
                if user1_sign == "":
                    user1_sign = random.choice(["X", "O"])
                    user2_sign = "X" if user1_sign == "O" else "O"
                    break

                user1_sign = input("please enter X or O\nor Press enter for default: ")

                if user1_sign.upper() not in ["X", "O", "0", 0]:
                    continue
                user2_sign = "X" if user1_sign == "O" else "O"
                _ = 0

        UserInfo.user1_name = "Player_1" if user1_name == "" else user1_name
        UserInfo.user2_name = input("Enter player2 Name: ")
        UserInfo.user2_name = "Player_2" if UserInfo.user2_name == "" else UserInfo.user2_name



class Board(Options, UserInfo):

    # def __init__(self, options_list):
    #     self.options_list = options_list

    def print_board(cls, user_turn_name):

        x1 = cls.board_option_stat["x1"]
        x2 = cls.board_option_stat["x2"]
        x3 = cls.board_option_stat["x3"]
        x4 = cls.board_option_stat["x4"]
        x5 = cls.board_option_stat["x5"]
        x6 = cls.board_option_stat["x6"]
        x7 = cls.board_option_stat["x7"]
        x8 = cls.board_option_stat["x8"]
        x9 = cls.board_option_stat["x9"]

        board = f"""                                                    <sample>
                {UserInfo.user1_name} vs {UserInfo.user2_name}
            |     |                                 1 | 2 | 3
          {x1} |  {x2}  | {x3}                              ___|___|___
         ___|_____|___                              4 | 5 | 6
            |     |                                ___|___|__
          {x4} |  {x5}  | {x6}                               7 | 8 | 9
         ___|_____|___
            |     |        it's {user_turn_name.upper()} turn
          {x7} |  {x8}  | {x9}
        """
        print(board)














# board_used_options = {
#     "x1": "1",
#     "x2": "2",
#     "x3": "3",
#     "x4": "4",
#     "x5": "5",
#     "x6": "6",
#     "x7": "7",
#     "x8": "8",
#     "x9": "9",
#     }
# Board.print_board(board_used_options, "Sharukh")








def play_tiktok():
    options = Options()

    userinfo = UserInfo()
    userinfo.user_info()

    board = Board()
    # board.print_board("sjo")

    game_starter = input(f"Who Want to play First?\n1.{userinfo.user1_name}\n2.{userinfo.user2_name}\n: ")

    _ = 0
    if game_starter not in [userinfo.user1_name, userinfo.user2_name, "1", "2"]:
        _ = 1
    while _:
        print("please enter player name OR option 1 or 2")
        game_starter = input(f"Who Want to play First?\n1.{userinfo.user1_name}\n2.{userinfo.user2_name}\n: ")
        if game_starter in [userinfo.user1_name, userinfo.user2_name, "1", "2"]:
            _ = 0
    game_starter = f"{userinfo.user1_name}" if game_starter in ["1", f"{userinfo.user1_name}"] else f"{userinfo.user2_name}"

    board.print_board(game_starter)
    print(Options.avilable_options())

    # Asking for position
    # position =





play_tiktok()










