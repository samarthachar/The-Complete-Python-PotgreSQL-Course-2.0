users = [
    (0, "Satoru", "muryokusho"),
    (1, "Nagi", "mendokuso"),
    (2, "Tony", "geniusbillionaireplayboyphilantropist")
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
if username_input in username_mapping.keys():
    password_input = input("Enter your password: ")
    _ , username, password = username_mapping[username_input]
    if password_input == password:
        print("Logged In")
    else:
        print("Invalid")
else:
    print("Invalid")
