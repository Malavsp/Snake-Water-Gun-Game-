import sys
from random import choice

# variables for all messages and its corresponding values

welcome_msg = f"Welcome to the Snake ,Water, Gun Game\nDESCRIPTION: \nsnake wins over water\nwater wins over gun \ngun wins over snake "
mode_msg = f"1) Human vs Human \n2) Human vs Computer\nEnter your choice (1/2) : "
mode_str = ["", "Human vs Human mode Activated",
            "Human vs Computer mode Activated"]
nor_msg = "Enter No. of Rounds : "
choices_msg = f"Enter Your choice: s(snake)   w(water)   g(gun) : "
invalid_msg = "You have entered invalid option"
exit_msg = f"\nDo you want to exit the game ?(y/n) : "
mode_val = ['1', '2']
choices_val = ['s', 'w', 'g']
exit_val = ['y', 'n']

# Universal input Function


def userinput(msg, val):

    while True:
        response = input(msg).lower()
        if response in val:
            return response
        print(invalid_msg)
        if (msg != exit_msg):
            exit()  # will ask to exit on any invalid input choice other than of the exit_msg

# exit() function.


def exit():
    r = userinput(exit_msg, exit_val)
    if (r == 'y'):
        sys.exit("Game terminated")


# point_checker() function

def point_checker(ch1, ch2):

    ans, com = ['s', 'w', 'g'], ['w', 'g', 's']
    if ch1 == ch2:
        return 0

    for i in range(len(ans)):
        if (ch1 == ans[i] and ch2 == com[i]):
            return 1
        if (ch2 == ans[i] and ch1 == com[i]):
            return 2


# play_game() function
def play_game(md, nr):

    res1 = res2 = 0
    for i in range(int(nr)):

        print(f"\nPlayer : 1 \t Round : {i + 1}")
        ch1 = userinput(choices_msg, choices_val)
        if md == '1':
            print(f"\nPlayer : 2 \t Round : {i + 1}")
            ch2 = userinput(choices_msg, choices_val)
        else:
            ch2 = choice(choices_val)
            print(f"Computer's choice is : {ch2}")

        p_c = point_checker(ch1, ch2)

        if p_c == 1:
            res1 += 1
        elif p_c == 2:
            res2 += 1

    return res1, res2


# winner()
def winner(md, res1, res2):
    if res1 == res2:
        return "Its a tie"
    elif res1 > res2:
        return "Player 1 win the game"
    elif md == '1':
        return "Player 2 win the game"
    else:
        return "Computer win the game"


def main():
    print(welcome_msg)
    while True:
        md = userinput(mode_msg, mode_val)
        print(mode_str[int(md)])

        while True:
            nr = input(nor_msg)
            if nr.isdigit():
                break      # validation for valid integer input
            print(invalid_msg)
            exit()

        p1, p2 = play_game(md, nr)
        print(f"\n{winner(md, p1, p2)}")

        exit()


if __name__ == '__main__':
    main()
