class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter a message: ")

    def print_message(self):
        print(self.message.upper())

daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()

class HelperSession:
    def __init__(self):
        print("Session started.")

    def __del__(self):
        print("Session ended.")

def create_session():
    return HelperSession()

my_session = create_session()

class PairFinder:
    def find_pair(self, numbers, target):
        for i, num1 in enumerate(numbers):
            for j, num2 in enumerate(numbers):
                if i != j and num1 + num2 == target:
                    print("Matching index pair:", i, "and", j)
                    return True
        print("No pair found.")
        return False

number_list = [10, 20, 30, 40, 50, 60, 70]
print("Numbers list:", number_list)

user_target = int(input("Enter a target sum (like 90 or 100): "))

finder = PairFinder()
finder.find_pair(number_list, user_target)

del my_session
