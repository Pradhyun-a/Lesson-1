costPrice = float(input("Enter the cost price of the item: "))
sellingPrice = float(input("Enter the selling price of the item: "))

# if sellingPrice > costPrice:
#     print("You have made a profit! ")

# else:
#     print("You have not made a profit")    


if sellingPrice > costPrice:
    print("You have made a profit! ")

elif sellingPrice < costPrice:
    print("You have incurred a loss")

else:
    print("You have not made a profit")        