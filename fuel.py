

def main():
    while True:
        try:
            user_input = input("Enter a fraction: ")
            x, operation, y = user_input.rpartition("/")
            if int(x) <= int(y):
                check(x,y)
                convert(x, y)
                break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except float:
            pass



def convert(x, y):
    x = int(x)
    y = int(y)
    result(x, y)
    return x, y


def f_e(r):
    if r >= 99:
        print("F")
    elif r <= 1:
        print("E")
    else:
        print(round(r), "%", sep="")


def result(x, y):
    equation = (x/y) * 100
    f_e(equation)


def check(x, y):
    if x is not int:
        return False
    if y is not int:
        return False


main()
