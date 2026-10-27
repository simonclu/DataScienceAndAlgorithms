class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
class ATM:
    def __init__(self, startingMoney=1000.00):
        self.money = startingMoney
        self.users = {}
        self.currentUser = None
    def signup(self, user, password):
        self.users[user.name] = [password]
        print("Signup successful!")
    def login(self, user, password):
        if user.name not in self.users:
            print("This account does not exist yet.")
            if input("Would you like to sign up? [y/n] ") == "y":
                self.signup(user, password)
        elif self.users[user.name] != password:
            print("Login unsuccessful - wrong password")
        else:
            self.currentUser = user
            print("Login successful!")