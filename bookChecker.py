books = ["Python", "Java", "HTML"]
copies = [3, 0, 5]

stock = {b: c for b, c in zip(books, copies)}

available = [b for b, c in stock.items() if c > 0]
print("Available books:", available)

choice = input("Which book do you want? ")

if choice not in stock or stock[choice] == 0:
    print("Sorry, book is unavailable.")
    exit()

fees = [1, 2, 3]
extra = float(input("Enter extra fee: "))
new_fees = list(map(lambda x: x + extra, fees))
print("Updated fees:", new_fees)

book_index = books.index(choice)
chosen_fee = new_fees[book_index]
stock[choice] = stock[choice] - 1

print("\n--- Summary ---")
print("Borrowed:", choice)
print("Late fee rate:", chosen_fee)
print("Updated stock:", stock)
