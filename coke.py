amount = 50
while amount > 0:
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5 or insert == 50:
        amount = amount - insert
        if amount < 0 :
            print("Amount Due: ", amount * -1)
        else:
            print("Amount Due: ", amount)

    elif insert != 25 or insert != 10 or insert != 5 or insert != 50:
        print("Amount Due: ", amount)
    elif amount == 0:
        print("change Owed: ", amount)