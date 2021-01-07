print('''
 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
    mls                              .$"
                                     "
''')
print("Welcome to the Dragon's Lair.")
print("Your mission is to find the caeruleum chest.")

choice1 = input('You\'re at the cave entrance - Do you enter or leave?  Type "enter" or "leave."\n').lower()

if choice1 == "enter":
  choice2 = input('You venture deeper into the cave and come to a fork, where do you want to go?  Type "left" or "right".\n').lower()
  if choice2 == "left":
    choice3 = input('You continue further and find a sleeping dragon guarding 3 colored chests. Which one is the caeruleum chest?  Type "red", "blue", or "green".\n').lower()
    if choice3 == "blue":
      print("You have found the caeruleum treasure! You win!")
    elif choice3 == "red":
      print("The chest bursts into flames. Game over.")
    elif choice3 == "green":
      print("The green chest is enchanted, this rouses the dragon from it's slumber! Game over.")
    else:
      print("The dragon is aware of your presence! Game over.")
  else:
    print("You hear a loud rumbling and the shaft suddenly collapses. Game over.") 
else:
  print("You run away in fear. Game over.")
