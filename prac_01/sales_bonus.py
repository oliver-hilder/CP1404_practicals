bonus = 0
sales = int(input("Sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = 0.1
    else:
        bonus = 0.15
    total = sales * bonus
    print("Your total bonus is $", total, sep="")
    sales = int(input("Sales: $"))



