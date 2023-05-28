from abc import ABC


class Bank(ABC):
    def __init__(self):
        self.users = {}  # Dictionary to store user information
        self.credit_percent = 0.1  # Default credit interest rate
        self.deposit_percent = 0.05  # Default deposit interest rate

    def add_user(self, user):
        if user not in self.users:
            self.users[user] = {
                "credits": {},
                "deposits": {},
                "money": 0
            }
            # Initialize user's credit, deposit, and money information

    def credit(self, user, name_of_credit, value):
        assert user in self, "No such user!"  # Check if user exists
        self.users[user]["credits"][name_of_credit] = value
        self.users[user]["money"] += value
        # Add a credit with a given value to the user and update their money

    def repay_credit(self, user, name_of_credit, value):
        assert user in self, "No such user!"  # Check if user exists
        if name_of_credit in self.users[user]["credits"]:
            credit_value = self.users[user]["credits"][name_of_credit]
            if credit_value >= value:
                self.users[user]["credits"][name_of_credit] -= value
                self.users[user]["money"] -= value
                # Subtract the repayment value from the credit and update user's money
            else:
                print("Not enough credit amount")
        else:
            print("No such credit")

    def deposit(self, user, name_of_deposit, value):
        assert user in self, "No such user!"  # Check if user exists
        if self.users[user]["money"] >= value:
            self.users[user]["deposits"][name_of_deposit] = value
            self.users[user]["money"] -= value
            # Add a deposit with a given value to the user and update their money
        else:
            print("Not enough money")

    def with_draw(self, user, value):
        assert user in self, "No such user!"  # Check if user exists
        if self.users[user]["money"] >= value:
            self.users[user]["money"] -= value
            return value
            # Withdraw the given value from the user's money and return it
        else:
            print("Not enough money")
            return 0

    def transfer(self, user1, user2, value):
        assert user1 in self and user2 in self, "No such users!"  # Check if both users exist
        self.users[user2]["money"] += self.with_draw(user1, value)
        # Transfer the given value from user1 to user2 by updating their money

    def top_up(self, user, value):
        assert user in self, "No such user!"  # Check if user exists
        self.users[user]["money"] += value
        # Add the given value to the user's money

    def update(self):
        for user, statics in self.users.items():
            if self.users[user]["credits"]:
                for credit_name in self.users[user]["credits"].keys():
                    self.users[user]["credits"][credit_name] *= (self.credit_percent + 1)
                    # Update the value of each credit by applying the credit interest rate
            if self.users[user]["deposits"]:
                for deposit_name in self.users[user]["deposits"].keys():
                    self.users[user]["deposits"][deposit_name] *= (self.deposit_percent + 1)
                    # Update the value of each deposit by applying the deposit interest rate

    def info(self):
        for user, statics in self.users.items():
            print(user)
            print("\tCredits:", statics["credits"])
            print("\tDeposits:", statics["deposits"])
            print("\tMoney:", statics["money"])
            # Print user information, including credits, deposits, and money

    def __contains__(self, user):
        return user in self.users
        # Check if a user exists in the bank's user dictionary


class Person:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    def __repr__(self):
        return f"{self.surname} {self.name}"


class PKO(Bank):
    def __init__(self):
        super().__init__()
        self.credit_percent = 0.2
        # Override the default credit interest rate for PKO Bank


class Santander(Bank):
    def __init__(self):
        super().__init__()
        self.deposit_percent = 0.07
        # Override the default deposit interest rate for Santander Bank


pko = PKO()  # Create an instance of PKO Bank
santander = Santander()  # Create an instance of Santander Bank

ivan = Person("Ivan", "Karobkin")
maks = Person("Maks", "Anikeev")
john = Person("John", "Doe")
emma = Person("Emma", "Smith")

pko.add_user(ivan)  # Add Ivan as a user to PKO Bank
pko.add_user(maks)  # Add Maks as a user to PKO Bank
santander.add_user(john)  # Add John as a user to Santander Bank
santander.add_user(emma)  # Add Emma as a user to Santander Bank

pko.credit(ivan, "House", 10000)  # Add a credit for Ivan in PKO Bank
pko.transfer(ivan, maks, 1000)  # Transfer 1000 from Ivan to Maks in PKO Bank
pko.deposit(maks, "Car", 100)  # Add a deposit for Maks in PKO Bank
pko.repay_credit(ivan, "House", 5000)  # Repay 5000 from Ivan's credit in PKO Bank
santander.top_up(john, 5000)  # Add 5000 to John's money in Santander Bank
santander.credit(emma, "Education", 20000)  # Add a credit for Emma in Santander Bank

pko.update()  # Update credits and deposits in PKO Bank
pko.info()  # Print user information in PKO Bank

santander.update()  # Update credits and deposits in Santander Bank
santander.info()  # Print user information in Santander Bank
