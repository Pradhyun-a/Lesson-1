class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = str(pin)

    def show_pin_status(self):
        print("Current PIN is:", self.__pin)

    def set_pin(self, new_pin):
        new_pin = str(new_pin)
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN safely updated!")
        else:
            print("Error: PIN must be 4 digits.")

    def __str__(self):
        return f"Account for {self.owner}"

my_account = Account("Alice", "1234")
print(my_account)

my_account.__pin = "9999"
my_account.show_pin_status()

my_account.set_pin("9999")
my_account.show_pin_status()

my_account.set_pin("99")
my_account.set_pin("abcd")
