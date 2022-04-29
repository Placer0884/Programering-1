import random


# Input values to list
temperatures = []
for i in range(20):
    temperatures.append(random.randint(-50, 50))


# Calculate max, min and average temperatures
maxTemp = max(temperatures)
minTemp = min(temperatures)
averageTemp = sum(temperatures)/len(temperatures)


# Create dictionary
dictionary = {
    "maximum temperature": maxTemp,
    "minimum temperature": minTemp,
    "average temperature": averageTemp,
    "all values": temperatures
}

# Create tuple
mytuple = (dictionary, )
dictionary = mytuple[0]


# Main
while True:
    awnser = (input("Write the element you with to see or exit to exit")).lower()

    if awnser == "exit":
        break

    elif awnser in dictionary.keys():
        print(dictionary[awnser])

    else:
        print(awnser, "was not found", end="\n\n")
        print("You have to choose one of the following:")
        for key in dictionary.keys():
            print(key)
