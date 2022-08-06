import hashlib


# import sqlite3
# from simplesqlite import SimpleSQLite
#
#
# table_name = "game"
# con = SimpleSQLite("game.sqlite", "w")
#

def signup():
    name = input("Enter name: ")
    username = input("Enter username address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    # with open("credentials.csv", "r") as f:
    #     stored_username, stored_pwd = f.read().split("\n")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.csv", "w") as f:
            f.write(name + "\n")
            f.write(username + "\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully!")
    # elif username == stored_username:
    #     print("you have signed up!")
    else:
        print("Password is not same as above! \n")


def login():
    username = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.csv", "r") as f:
        stored_username, stored_pwd = f.read().split("\n")
    f.close()
    if username == stored_username and auth_hash == stored_pwd:
        print("Logged in Successfully!")
    else:
        print("Login failed! \n")
