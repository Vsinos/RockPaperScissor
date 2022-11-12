#Variables
counter = 0
option = ("RSPPSRSRPRSPPRS")
while True:
    user_choice = input("Choose (R)ock, (S)cissor, (P)aper: ").lower().upper()
    if user_choice not in ["R", "S", "P"]:
        print("Please, choose: R, S or P. ")
#PARAMETER WHEN WE RUN OUT OF CHARACTERS IN THE STRING
    computer_option = option[counter]
    if counter == len(option)-1:
        counter = 0
    else:
        counter += 1
    print("Computer choose: ", (computer_option))
#OPTION-DRAW
    if computer_option == user_choice:
        print("It's a Draw!") 
#USER-COMPUTER // WIN-LOSE OPTIONS
    elif user_choice == "R":
        if computer_option == "S":
            print("You Won!")
        else:
            print("You lost!")
    elif user_choice == "P":
        if computer_option == "R":
            print("You Won!!")
        else:
            print("You lost!")
    elif user_choice == "S":
        if computer_option == "R":
            print("You lost!")
        else:
            print("You Won!")
#IF YOU WANT TO EXIT
    exit = (input("Do you want to continue?? (Y) or (N): ")).lower().upper()
    if exit == "N":
        print("Game Over")
        break
    else:
        exit == "Y"
        continue
