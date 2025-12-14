
import string
import datetime

#  Caesar Cipher Functions

def encode(input_text, shift):
    """
    Returns (alphabet_list, encoded_text).
    Letters are shifted. Everything else stays the same.
    Output is always lowercase.
    """
    alphabet = list(string.ascii_lowercase)
    encoded = ""

    for ch in input_text:
        lower = ch.lower()
        if lower in alphabet:
            # find position of letter
            old_index = alphabet.index(lower)
            new_index = (old_index + shift) % 26
            encoded += alphabet[new_index]
        else:
            # punctuation, spaces, digits, etc.
            encoded += ch

    return alphabet, encoded


def decode(input_text, shift):
    """
    Reverse Caesar cipher:
    shift backwards instead of forwards.
    """
    alphabet = list(string.ascii_lowercase)
    decoded = ""

    for ch in input_text:
        lower = ch.lower()
        if lower in alphabet:
            old_index = alphabet.index(lower)
            new_index = (old_index - shift) % 26
            decoded += alphabet[new_index]
        else:
            decoded += ch

    return decoded


#  BankAccount Class

class BankAccount:
    """
    Basic bank account.
    Rules:
    - creation_date cannot be in the future
    - negative deposits do nothing
    - deposit() and withdraw() must PRINT balance
    """

    def __init__(self, name="Rainy", ID="1234",
                 creation_date=None, balance=0):

        # default creation date = today
        if creation_date is None:
            creation_date = datetime.date.today()

        # must be a date
        if not isinstance(creation_date, datetime.date):
            raise TypeError("creation_date must be a datetime.date")

        # cannot be a future date
        if creation_date > datetime.date.today():
            raise Exception("creation_date cannot be in the future")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits positive amounts.
        Prints resulting balance.
        """
        try:
            amount = float(amount)
        except:
            print(f"Balance: {self.balance}")
            return

        if amount > 0:
            self.balance += amount

        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraws amount (base class allows overdraft).
        Prints resulting balance.
        """
        try:
            amount = float(amount)
        except:
            print(f"Balance: {self.balance}")
            return

        self.balance -= amount
        print(f"Balance: {self.balance}")

    def view_balance(self):
        return self.balance



#  SavingsAccount Class

class SavingsAccount(BankAccount):
    """
    Rules:
    - No withdrawals unless account is 180 days old
    - No overdraft allowed
    """

    def withdraw(self, amount):
        # check age of account
        age = (datetime.date.today() - self.creation_date).days

        if age < 180:
            # too early to withdraw
            print(f"Balance: {self.balance}")
            return

        try:
            amount = float(amount)
        except:
            print(f"Balance: {self.balance}")
            return

        # no overdrafts allowed
        if amount > self.balance:
            print(f"Balance: {self.balance}")
            return

        self.balance -= amount
        print(f"Balance: {self.balance}")


#  CheckingAccount Class

class CheckingAccount(BankAccount):
    """
    Rules:
    - Overdrafts allowed
    - When a withdrawal makes balance negative,
      apply a $30 overdraft fee
    """

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except:
            print(f"Balance: {self.balance}")
            return

        before = self.balance
        self.balance -= amount

        # if account crossed from >=0 into <0
        if before >= 0 and self.balance < 0:
            self.balance -= 30   # overdraft fee

        print(f"Balance: {self.balance}")
