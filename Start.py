print("You are flying over the Canadian wilderness, but some dumbass named Arron decided to crash and condemn us all, find your way back to society with only a compass and flashlight you found.") 
print("'Damn, my head hurts, but I gotta get outta here' you think, 2 options present itself, no time to go back, North or West?")
choice = input()
if choice == "North":
    print("You go North and you see a cave West and more forest North and East, where will you go?")
    
    choice2 = input("")
    if choice2 == "West":
        print("Not sure how this is gonna help you but do you go deeper or turn around?")

    elif choice == "West":
        print("You go West and hear a low bellow, 'he's right behind me, isn't he?' a bear slahes your head off. Game Over")
    else:
        input("No time to dilly dally, gotta go somewhere.") 
        