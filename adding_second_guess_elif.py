answer = 5
print("Please the no. between 1 to 10")
guess = int(input())

if guess < answer:
    print("please guess higher ")
    guess = int(input())
    if guess == answer:
        print("well done you have guessed it right ")

elif guess > answer:
    print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done you have guessed it Right ")

    else:
        print("you have got it wrong ")

else:
    print("you got it in first time ")
