great = input("What is the answer to the Great Question of life, the Universe, and Everything? ")
great = great.strip()
match great:
    case "42" | "forty-two" | "forty two" | "FoRty TwO" | " 42" | "42 " |" 42 ":
        print("Yes")
    case _:
        print("No")

