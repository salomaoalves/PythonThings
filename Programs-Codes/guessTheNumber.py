import random

def main():
    print("----------------WELCOME--------------------------")
    n = int(input("Numbers of players (1/2): "))
    print()
    if n==1:
        begin1player()
    else:
        begin2players()
    print()
    again = input("The game is over, do you wanna play again (y/n):")
    print()
    if again == "y":
        main()
    else:
        print("Thanks to play with us! Bye Bye!!!!")

def begin1player():
    max = int(input("Biggest number: "))
    number = random.randint(0,max)
    
    while True:
        print()
        shot = int(input("Your shot is: "))
        if shot == number:
            print("You are correct!!!")
            break
        elif shot<number:
            print("The real number is bigger than your shot")
        elif shot>number:
            print("The real number is smaller than your shot")

def begin2players():
    pl1,pl2 = 0,0
    print()
    rounds = int(input("How many round do you wanna play (we need a even number): "))
    tries = int(input("How many tries each players has: "))
    print("The player 1 starts by choosing the number!")
    input()

    for i in range(rounds):
        print("Rounds ",i)
        number = int(input("Choose a number: "))
        guess = tries
        while guess>0:
            shot = int(input("Your shot is: "))
            if shot == number:
                print("You're correct!!!")
                if i%2 == 0:
                    pl2 += 1
                else:
                    pl1 += 1
                break
            elif shot<number:
                print("The real number is bigger than your shot")
                guess -= 1
            elif shot>number:
                print("The real number is smaller than your shot")
                guess -= 1
            if guess == 0:
                print("----------------------------------------------")
                print("You did not get it right!!! Next player!!")
        print()
    if pl1 > pl2:
        print("Players 1 win!!!!!")
    elif pl2 > pl1:
        print("Players 2 win!!!!!")
    else:
        print("It is a draw!!!")

main()