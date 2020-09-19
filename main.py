import random 







print("!...WELCOME TO THE NUMBER GUESSING GAME...!")

print("I AM A COMPUTER GUESS MY NUMBER!!!!")

computerNum = random.randint(0,20)
print(computerNum)


win = False
still_playing = True
tries = 5

while still_playing == True:
    while tries > 0:
        print()
        playNum = int(input("Enter a number between 0-20: "))

        if playNum > computerNum:
            print("Your Number is too Big!")
            tries-= 1
            print("You have " + str(tries) +" tries left.")
        elif playNum < computerNum:
             print("Your Number is too Small!")
             tries-= 1
             print("You have " + str(tries) +" tries left.")
        else: 
            playNum == computerNum
            print("You Guessed It!")
            win = True
            break
if win == True:
    print("Congrats! You won at " + str(6-tries) +" tries")
else:
    print("No More Tries")
    print("The Number was " + str(computerNum))

anser = input("Do you want to play again? Y or N")


if answer.upper() == "N":
        print(answer)
        print("Ok Bye!")
        still_playing = False
else: 
    win = False
    tries = 5
    computerNum = random.radint(0, 20)
