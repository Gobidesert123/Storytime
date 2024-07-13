print('''
************************************************************
              _      _
             (c\-.--/a)
              |q: p   /\_            _____
            __\(_/  ).'  '---._.---'`     '---.__
           /  (Y_)_/             /        : \-._ 
   !!!!,,, \_))'-';             (       _/   \  ' _
  !!II!!!!!IIII,, \_             \     /      \_  '.
   !IIsndIIIII!!!!,,\     /_      \   |----.___ '-. \.__
   !!!IIIIIIIIIIIIIIII\   | '--._.-'  _)       \  |  `'--'
       ''''!!!!IIIIIII/   .'',  ((___.-'
             '''!!!!/  _/!!!!IIIIIII!!!!!,,,,,;,;,,,.....
                   | /IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                   | \   ''IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                   \_,)     ''''''!!!!IIIIIIIIIIIIIIII!!!!!!!!
                                     ''''''''!!!!!!!!!!!!!!!
********************************************************************
''')

print("Welcome to the Jungle")
# We added .lower to the end, just incase the user inputed an uppercase letter
choice_1 = input("Would you like to go left to right? ").lower()
# print(choice_1)
if choice_1 == "left":
    choice_2 = input("Would you like to run or wait? ").lower()
    # print(choice_2)
    if choice_2 == "run":
        choice_3 = input("Which door would you choose to hide in? blue, red or yellow ").lower()
        if choice_3 == "blue":
            print("You died")
        elif choice_3 == "red":
            print("You were eaten alive")
        elif choice_3 == "yellow":
            print("You have survived")
        else:
            print("You have given an invalid output")
    elif choice_2 == "wait":
        print("You have been eaten alive")
    else:
        print("You have given an invalid output")
elif choice_1 == "right":
    print("You have been eaten alive")
else:
    print("You have given an invalid output")

