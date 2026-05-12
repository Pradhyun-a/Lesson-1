def total_calc(billAmount, tipPercent):
    tip = (billAmount * tipPercent) /100
    total = billAmount + tip
    print(billAmount)
    print(tipPercent)
    print(tip)
    print(total)
total_calc(2000, 10)
