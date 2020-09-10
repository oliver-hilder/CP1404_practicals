COLOUR_COLLECTION = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "beige": "#f5f5dc",
                     "black": "#000000", "brown": "#a52a2a", "burlywood": "#deb887", "cadetblue": "#5f9ea0",
                     "chocolate": "#d2691e", "coral": "#ff7f50"}

print("Hexadecimal Colour Converter")
print(COLOUR_COLLECTION)
colour_code = input("Enter colour name: ")
while colour_code != "":
    if colour_code in COLOUR_COLLECTION:
        print(colour_code, "is", COLOUR_COLLECTION[colour_code])
    else:
        print("Invalid colour")
    colour_code = input("Enter colour name: ")
