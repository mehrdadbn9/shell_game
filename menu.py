from registration import signup, login
from config import scoreboard


def menu():
    print("********** menu **********")
    print("1.Signup")
    print("2.Login")
    print("3.Scoreboard")
    print("4.Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            signup()
        case 2:
            login()
        case 3:
            print(scoreboard)
        case 4:
            exit()


if __name__ == '__main__':
    menu()
