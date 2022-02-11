building_type = input("What type of building would you like? \n"
                      "Press r for residential or c for commercial: ")

inputOne = "r"
inputTwo = "c"

while building_type == inputOne or inputTwo:

    if building_type == "r":
        depth = 0.5
        length = int(input("Please enter the length of the building: "))
        width = int(input("Please enter the width of the building: "))
        volume = depth * length * width
        print("The volume of concrete needed is {}".format(volume))

    elif building_type == "c":
        depth = 0.25
        length = int(input("Please enter the length of the building: "))
        width = int(input("Please enter the width of the building: "))
        volume = depth * length * width
        print("The volume of concrete needed is {} square meters".format(volume))
else:
    print("Sorry that is not an option.")

print("Thanks")

