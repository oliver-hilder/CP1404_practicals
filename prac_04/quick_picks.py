import random

line = []
picks = int(input("How many quick picks? "))
for i in range(1, picks + 1):
    for number in range(6):
        number = random.randint(1, 45)
        while number in line:
            number = random.randint(1, 45)
        line.append(number)
        line = sorted(line)
    print(line)
    line = []
