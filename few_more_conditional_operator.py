answer = 5
print("Please the no. between 1 to 10")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Guess lower")

    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it right")
    else:
        print("not guessed it correctly ")

else:
    print("you have got it in first time ")