def start():
    print("You are in a dark room there are 2 doors:")
    print("which door will u choose right or left")
    op=input(">").lower()
    if 'l' in op:
        bear_room()
    elif 'r' in op: 
        monster_room()
    else: 
        game_over("enter correctly man!")
def bear_room():
    print("\nThere is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating tasty honey!")
    print("What would you do? (1 or 2)")
    print("1). Take the honey.")
    print("2). Taunt the bear.")
  
    answer = input(">")
  
    if answer == "1":
    # the player is dead!
         game_over("The bear killed you.")
    elif answer == "2":
    # lead him to the diamond_room()
         print("\nYour Good time, the bear moved from the door. You can go through it now!")
         diamond_room()
    else:
    # else call game_over() function with the "reason" argument
         game_over("Don't you know how to type a number?")       
def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2). Kill the monster and show your courage!")
    op=input(">")
    if op =='2':
        game_over("The monster was hungry, he/it ate you.")
    elif op=='1':
        print("\nYour Good time, the monster moved from the door. You can go through it now!")
        diamond_room()
    else:
        game_over("Don't you know how to type a number?") 
def diamond_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door.")
    print("2). Just go through the door.") 
    op = input(">")
    if op =='1':
        game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
    elif op =='2':
        print("nNice, you're are an honest man! Congrats you win the game!")
        play_again()
    else:
        game_over("enter crrectly man!") 
def game_over(value):
    print("\n")
    print("\n",value)
    print("Game over!")
    play_again()
def play_again():
    print("do you want to play again!")
    op=input(">").lower()  
    if 'y' in op:
        start()
    else: exit()        
start()