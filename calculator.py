def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Choose operation ")
print("1. add ")
print("2. subtract ")
print("3. multiply ")
print("4. divide ")

choice = input("Enter choice: (1/2/3/4)")
if choice == "1":
    print(add(num1, num2))
elif choice == "2":
    print(subtract(num1, num2))
elif choice == "3":
    print(multiply(num1, num2))
elif choice == "4":
    print(divide(num1, num2))
else:
    print("invalid choice")
