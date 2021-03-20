import sqlite3

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def __str__(self):
        return """
            Username: {}
            E-mail: {}
            Password: {}
        """.format(self.username, self.email, self.password)
    def for_user(self):
        user_pass = ""
        user_email = ""
        
        for i in self.password:
            user_pass += "*"

        email = [[j for j in i] for i in self.email.split("@")]
        for i in range(1, len(email[0]) - 1):
            email[0][i] = "*"
        for i in "".join(email[0]):
            user_email += i
        user_email += "@"
        for i in "".join(email[1]):
            user_email += i

        """
        email = [i for i in self.email.split("@")]
        user_email += email[0][0]
        for i in email[0][1:-1]:
            user_email += "*"
        user_email += email[0][-1]
        user_email += "@"
        user_email += email[1]
        
        """


        return """
            Username: {}
            E-mail: {}
            Password: {}
        """.format(self.username, user_email, user_pass)


class App:
    def __init__(self):
        self.connection()
        self.who = ""

    def connection(self):
        self.connect = sqlite3.connect("users")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (Username TEXT, Email TEXT, Password TEXT)")
        self.connect.commit()

    def diconnect(self):
        self.connect.close()

    def register(self, username, email, password):
        self.cursor.execute("Select * From users where Username = ?", (username,))
        usernames = self.cursor.fetchall()
        self.cursor.execute("Select * From users where Email = ?", (email,))
        emails = self.cursor.fetchall()
        if len(usernames) != 0 and len(emails) != 0:
            print("This Username and Email is used!")
        elif len(usernames) != 0 and len(emails) == 0:
            print("This Username is used!")
        elif len(usernames) == 0 and len(emails) != 0:
            print("This Email is used!")
        else:
            self.cursor.execute("INSERT INTO users Values(?, ?, ?)", (username, email, password))
            self.connect.commit()
            print("Success!\nWelcome {}".format(username))
            self.who = username

    def login(self, email, password):
        self.cursor.execute("Select * From users where Email = ? and Password = ?", (email, password))
        user = self.cursor.fetchall()

        if len(user) == 0:
            print("İts wrong or there isnt this account!")
        else:
            print("Welcome {}".format(user[0][0]))
            self.who = user[0][0]

    def all_user(self):
        self.cursor.execute("Select * From users")
        users = self.cursor.fetchall()

        for i in users:
            user = User(i[0], i[1], i[2])
            if self.who != "admin":
                print(user.for_user())
            else:
                print(user)
    def delete_account(self, username):
        self.cursor.execute("Select * From users where Username = ?", (username,))
        user = self.cursor.fetchall()

        if len(user) == 0:
            print("There isn't this user here!")
        elif self.who != "admin":
            print("You don't have authority!")
        elif username == "admin":
            print("You can't delete admin's account")
        else:
            self.cursor.execute("DELETE FROM users where Username = ?", (username,))
            self.connect.commit()
            print("Success!")
    def find_account(self, username):
        self.cursor.execute("Select * From users where Username = ?", (username,))
        user = self.cursor.fetchall()
        if len(user) == 0:
            print("There isn't this user here!")
        else:
            for i in user:
                user = User(i[0], i[1], i[2])
                if self.who != "admin":
                    print(user.for_user())
                else:
                    print(user)
