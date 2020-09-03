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
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(line[0], line[1], line[2], line[3], line[4], line[5]))
    line = []
