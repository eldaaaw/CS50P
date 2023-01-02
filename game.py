import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass


guess = int(random.randint(1, n))
# print(guess)
while True:
    try:

        user_guess = int(input("Guess: "))
        if user_guess > 0 :
            if user_guess == guess:
                print("Just right!")
                break
            elif user_guess > guess:
                print("Too large!")
            elif user_guess < guess:
                print("Too small!")

    except:
        pass
