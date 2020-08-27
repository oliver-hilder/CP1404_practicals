# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# out_file = open("data.txt", "w")
# name = str(input("Enter Name: "))
# out_file.write(name)
# out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
# in_file = open("data.txt", "r")
# name = in_file.read()
# print("Your name is {}".format(name))
# in_file.close()

# 3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the
# result, which should be... 59.
in_file = open("numbers.txt", "r")
result = 0
for i in range(2):
    number = in_file.readline()
    result = result + int(number)
print(result)
in_file.close()

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of
# numbers.
in_file = open("numbers.txt", "r")
lines = readlines(in_file).count()
result = 0
for i in range(1, ):
