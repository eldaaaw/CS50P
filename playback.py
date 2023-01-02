def userInput():
    text = input("Enter a text: ")
    newText = text.replace(" ","...")
    print(newText)

userInput()