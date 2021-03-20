from Kullanıcı import *
app = App()

def valudation(email):
    if email.find("@") != -1 and email.endswith(".com"):
        return True
    else:
        return False

print("Welcome to our program!")
while True:
    print("1- Login\n2- Register")
    choose = input("Your choose: ")
    if choose == "q":
        print("See you!")
        app.diconnect()
        break
    elif choose == "1":
        email = input("E-mail: ").strip()
        password = input("Password: ").strip()
        app.login(email, password)
    elif choose == "2":
        username = input("Username: ").strip()
        email = input("E-mail: ").strip()
        if not (valudation(email)):
            print("İt isn't real email! Try again!")
            continue
        password = input("Password: ").strip()
        app.register(username, email, password)

    while app.who != "":
        print("1- List of all user\n2- Delete an account\n3- Find an account")
        choose = input("Would you like to see? (yes, no) (quit = 'q')")

        if choose == "yes":
            app.all_user()
        elif choose == "q":
            app.who = ""
        elif choose == "2":
            username = input("Username: ")
            app.delete_account(username)
        elif choose== "3":
            username = input("Username: ")
            app.find_account(username)


