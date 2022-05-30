import getpass
import json

from operations_manager import OperationsManager


def get_users():
    users_file = open("users.json")
    users_json = json.load(users_file)
    users_file.close()

    result = {}
    for u in users_json:
        result[u["username"]] = u["password"]

    return result


if __name__ == "__main__":
    users = get_users()

    user = input("Username: ")
    password = getpass.getpass("Password: ")

    if user not in users or password != users[user]:
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())
