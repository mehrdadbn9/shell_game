from config import scoreboard
from main import play
from menu import menu
from registration import login


def stat(username):
    with open("credentials.csv", "r+") as f:
        stored_username, stored_pwd = f.read().split("\n")
    f.close()
    if username == stored_username:
        with open("credentials.csv", "w") as f:
            wins = f.write(str(scoreboard['user']//3) + "\n")
            losses = f.write(str(scoreboard['system']//3) + "\n")
            win_rate = f.write(str(int(wins)/int(losses)))
        f.close()


def user_panel():
    print("1.play with system")
    print("2.stats of player")
    print("3. logout")
    option = int(input("Enter your choice: "))
    match option:
        case 1:
            play()
        case 2:
            username_input = input("please say the username: ")
            stat(username_input)
        case 3:
            menu()


if __name__ == '__main__':
    user_panel()
