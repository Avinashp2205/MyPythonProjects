# Extract vowels from a string

def vowelExtractor(inputText):
    vowels = ""
    for char in inputText:
        if char.lower() in "aeiou":
            vowels += char
    return vowels

MyText = input("Type your Text here : ")
print(vowelExtractor(MyText))