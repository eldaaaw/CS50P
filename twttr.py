answer = input("Input: ")
print("Output: ", end="")

for letter in answer:
    if not letter in ["a", "e", "i", "u", "o","A", "E", "I", "U", "O"]:
        print(letter, end="")

