def calculate_change(total_bill, amount_paid):
    change = amount_paid - total_bill
    return change

total_bill = 2.50
amount_paid = 4.00

change = calculate_change(total_bill, amount_paid)
print("Total Bill: $", total_bill)
print("Amount Paid: $", amount_paid)
print("Change to be returned: $", change)
