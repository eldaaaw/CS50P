import emoji

x = input("Input: ")
if "_" in x:
    x = x.replace("_","")
    print(emoji.emojize(f"{x}"))
else:
    print(emoji.emojize(f"{x}"))


