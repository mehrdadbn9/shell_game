from registration import signup, login


def users():
    print(
        "welcome user, "
        "if you are new user or daily user please enter proper number")
    print("1.sign up")
    print("2.login")
    print("3. exit from program")
    option = int(input("Enter your choice: "))
    match option:
        case 1:
            signup()
        case 2:
            login()
        case 3:
            exit()


users()
