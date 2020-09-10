"""Got stuck on this one, could do with some feedback :)"""
emails = {}
email = str(input("Email: "))
while email != "":
    name = email.split("@")
    check = str(input("Is your name {} (Y/n)?".format(name[0].title().split("."))))
    if check == "y":
        email.join()
        print(email)