# Write a python program to reverse a string

def reversedInput(inputString):
    reversedStr = ""
    for char in inputString:
        reversedStr = char + reversedStr
    return reversedStr

stringToReverse = input("Enter anything to be reversed here :")

print(reversedInput(stringToReverse))