import random
 
print("Welcome to Tauntaun!")
print("Out of hunger, you have stolen a Wampa's favourite meal, unbeknowst to you that you were seen by the Wampa.")
print("The Wampa wants his Tauntaun back and is chasing you down! Survive your trek and out run the Wampa.")
print()
 
# Variables
milesTravelled = 0
thirst = 0
TauntaunFatigue = 0
WampaDistance = -20
drinks = 3
player = 0
base = 0
rps = 0
total = 0                                                                   
 
#Start
while True:
    WampaBehind = milesTravelled - WampaDistance
    fullSpeed = random.randrange(10, 21)
    moderateSpeed = random.randrange(5, 13)
    #Options
    print()
    print("A. Drink from your cantina.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("Q. Quit.")
    print("S. Status\n")
 
    user_choice = input("Choose one of the options: \n")
 
    #Quit
    if user_choice.lower() == "q":
        print("You quit.")
        break
 
    #Status
    elif user_choice.lower() == "s":
        print()
        print("Miles travelled: ", milesTravelled, "miles")
        print("Drinks in cantina: ", drinks)
        print("The wampa is", WampaBehind, " miles behind you.")
 
    #Stop
    elif user_choice.lower() == "d":
        TauntaunFatigue = 0
        WampaDistance += random.randrange(7, 15)
        print("The Tauntaun is happy now.")
       
    #Full Speed
    elif user_choice.lower() == "c":
        milesTravelled += fullSpeed
        thirst += 1
        TauntaunFatigue += random.randrange(1, 4)
        WampaDistance += random.randrange(7, 15)
        base = random.randrange(1, 21)
        print("You have travelled", milesTravelled, "miles.")
        print("The Wampa is", WampaBehind, " miles behind you.")
 
    #Moderate Speed
    elif user_choice.lower() == "b":
        milesTravelled += moderateSpeed
        thirst += 1
        TauntaunFatigue += 1
        WampaDistance += random.randrange(7, 15)
        base = random.randrange(1, 21)
        print("You have travelled", milesTravelled, "miles.")
        print("The Wampa is", WampaBehind, " miles behind you.")
 
    #cantina
    elif user_choice.lower() == "a":
        if drinks == 0:
            print("There are no drinks available right now. Come back later!")
        else:
            drinks -= 1
            thirst = 0
            print("Well that was refreshing. You now have ", drinks, "drinks left.")
 
    #Error
    else:
        print("Invalid input; Try again") # Print error message
           
    #Thirst
    if thirst > 4 and thirst <= 6  :
        print("You are thirsty! Get a drink from the cantina immediately!")
    elif thirst > 6:
        print("You died of thirst!")
        break
 
    #Fatigue
    if TauntaunFatigue > 5 and TauntaunFatigue <= 8:
        print("Your Tauntaun is getting tired. You should take some rest for a while.")
    elif TauntaunFatigue > 8:
        print("Your Tauntaun is dead.")
        break
 
    #Wampa Distance
    if WampaBehind <= 15:
        print("The Wampa is getting close!")
    elif WampaBehind == 0:
        print("The Wampa has caught you. You lose.")
        break
    else:
        print("The Wampa is far behind.")
 
    # Rebel base
    if base == 20:
        drinks = 3
        thirst = 0
        TauntaunFatigue = 0
        print("You found a Rebel base! The drinks in the cantina are back in stock and the Tauntaun is refreshed.")
 
    #Rock paper scissors
    if rps == 10:
        # Player choices
        computer = random.randint(1, 4)
        player = int(input("You just came across a trader who wants to play rock paper scissors! Enter a number from 1 to 3 (1 = Rock, 2 = Paper, 3 = Scissor): "))
        if player == 1:
            print("You chose rock.")
        elif player == 2:
            print("You chose paper")
        else:
            print("You chose scissors.")
 
        # Computer's choices
        if computer == 1:
            print("Computer chose rock.")
        elif computer == 2:
            print("Computer chose paper.")
        else:
            print("Computer chose scissors.")
   
    # Match
        if player == computer:
            print("Tie.")
            total += 0
        elif player == 1 and computer == 2:
            print("You win.")
            total += 1
        elif player == 1 and computer == 3:
            print("You lose.")
            total += 0
        elif player == 2 and computer == 1:
            print("You win.")
            total += 1
        elif player == 2 and computer == 3:
            print("You lose.")
            total += 0
        elif player == 3 and computer == 1:
            print("You lose.")
            total += 0
        else:
            print("You win.")
            total += 1
 
        # Final score
        if total == 1:
            TauntaunFatigue = 0
            milesTravelled += 15
            drinks = 3
            question = input(print("You win! Your Tauntaun is now refreshed, the drinks are back in stock and you have jumped 15 metres.\nDo you want to play again? (y/n)"))
            if question != "y":
                break
        else:
            WampaDistance += 10
            print("You lose. The Wampa has travelled 10 more miles.")
 
    #Win
    if milesTravelled >= 200:
        print("You have finally outrun the Wampa and he has given up on you. You win!")
        break