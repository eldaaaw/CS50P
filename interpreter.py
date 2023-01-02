def main():
    userinput = input("Please enter an equation: ")
    if "+" in userinput:
        fnum, opreator,lnum = userinput.rpartition("+")
        addition(fnum, lnum)
    elif "-" in userinput:
        fnum, opreator, lnum = userinput.rpartition("-")
        substraction(fnum, lnum)
    elif "*" in userinput:
        fnum, opreator, lnum = userinput.rpartition("*")
        multiplication(fnum, lnum)
    elif "/" in userinput:
        fnum, opreator, lnum = userinput.rpartition("/")
        division(fnum, lnum)


def addition(fnum, lnum):
    result = float(fnum) + float(lnum)
    print(result)


def multiplication(fnum, lnum):
    result = float(fnum) * float(lnum)
    print(result)


def substraction(fnum, lnum):
    result = float(fnum) - float(lnum)
    print(result)


def division(fnum, lnum):
    result = float(fnum) / float(lnum)
    print(result)


main()