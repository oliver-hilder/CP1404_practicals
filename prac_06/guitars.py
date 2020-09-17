from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = str(input("Name: "))
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print("{}, ({}) : ${:,.2f} added.".format(name, year, cost))
    name = str(input("Name: "))
print("These are my guitars:")
for i in range(0, len(guitars)):
    vintage_string = ""
    if guitars[i].is_vintage() is True:
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitars[i].name, guitars[i].year, guitars[i].cost,
                                                              vintage_string))

