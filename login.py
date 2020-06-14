print("Welcome to DELTA")
print("\n")


option = input("Do you have an account? (y/n)      ")


def login():

    print("\n\n\n\n")
    password = input("Enter your password:      ")
    for line in open("Passwords.txt", "r").readlines():
        login_info = line.split()
    if password == login_info[0]:
        print("Success")
    else:
        print("Password Doesn't Match please try again")
        option


def register():
    pass_words = open("Passwords.txt", "a")
    print("\n\n\n\n")
    new_pass = input("Please enter a new password:   ")
    pass_words.write("\n")
    pass_words.write(new_pass)
    pass_words.close()
    print("Your password has been successfully added to the program. Please login")
    login()


if option == 'y' or option == 'Y':
    login()

elif option == 'n' or option == 'N':
    register()

else:
    print("Invalid option please enter one of the choices provided")


option
