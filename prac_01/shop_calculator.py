total = 0
counter = 0
items = int(input("Number of Items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of Items: "))
    while counter < items:
        item = float(input("Price of item: $"))
        if item > 100:
            item = item - item * 0.1
        total = total + item
        counter = counter + 1
print(f"Total price for {items} items is ${total}")