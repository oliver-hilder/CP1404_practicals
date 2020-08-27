MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_celcius():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


def convert_fahrenheit():
    global fahrenheit, celsius
    fahrenheit = float(input("Faremheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)

def main():
    while choice != "Q":
        if choice == "C":
            convert_celcius()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            convert_fahrenheit()
            print(f"Result: {celsius}C")
            # TODO: Write this section to convert F to C and display the result
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")