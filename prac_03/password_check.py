LENGTH_LIMIT = 5


def main():
    password = get_password()
    while len(password) < LENGTH_LIMIT:
        print("Length too small. Try again.")
        password = str(input("Enter Password: "))
    print_asterisk(password)


def print_asterisk(password):
    for character in password:
        print("*", end='')


def get_password():
    password = str(input("Enter Password: "))
    return password


main()
