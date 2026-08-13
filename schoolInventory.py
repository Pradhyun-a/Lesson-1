items = ["Pen", "Pencil", "Ruler", "Eraser", "Gluestick"]
stock = [10, 0, 5, 3, 0]
prices{
    "Pen": 10,
    "Pencil": 50,
    "Ruler": 5,
    "Eraser": 500,
    "Gluestick": 5,
}
inventory = dict(zip(items, stock))
available_items = {
    item = quantity
    for item, quantity in inventory.items()
    if quantity > 0
}
marked_prices = {
    item: price * 1.10
    for item, price in prices.items()
}
print("Available items:")
for item, quantity in available_items.iteams():
    print(item, "-", quantity, "available")
choice = input("\nWhich item do you want to buy? ")
if choice not in inventory:
    print("Item not found. ")
    exit()
if inventory[choice] == 0:
    print("Sorry, this item is out of stock. ")
    exit()
print("Item:", choice)
print("Price:", marked_prices[choice])
print("Stock available:", inventory[choice])
print("You can buy this item. ")
