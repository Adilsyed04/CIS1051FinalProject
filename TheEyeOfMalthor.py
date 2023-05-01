global weapon
weapon = False

def introScene():
   print("You wake up in a forest. As you look around, you see a stranger.")
   print("The stranger notices you and walks up to you.")
   print("Stranger: Hello sir, would you like some help?")
   choice= input("Do you want to receive some help from this stranger?(yes/no)\n")
   if choice.lower() == 'yes':
       print("Stranger: That's great to hear.")
       print("Stranger: My name is Hywell and I'll be glad to help.")
       introScene2()
   elif choice.lower() == 'no':
      print("Stranger: Oh, you should've said yes!")
      print("You are killed by the stranger.")
      print("###--- GAME OVER ---###")
      print("Hint: Accept help from others.")
      quit()
   else:
      print("I didn't quite understand that.\n")
      introScene()

def introScene2():
    directions = ["left","right"]
    userInput = ""
    print("Hywell: For starters, here is a map to help you see where you are.")
    print("###--- YOU HAVE BEEN GIVEN A MAP ---###")
    print("You look at the map to see two different options.")
    print("If you go left, then you'll find a town.")
    print("If you go right, then you'll encounter a dungeon.")
    while userInput not in directions:
        print("Which direction you want to go?(left/right)")
        userInput = input()
        if userInput == "left":
            print("You decide to go the town with Hywell.")
            print("Once you are there, you are welcomed by the town and spend your days there.")
            print("After a few days in the town, you hear the townspeople screaming that there is an incoming attack.")
            print("Once you go to see who is attacking, you see that a dragon with his army is approaching the town.")
            print("As the town isn't well prepared, the whole town is taken over by the dragon.")
            print("###--- YOU HAVE REACHED BAD ENDING 1 ---###")
            quit()
        elif userInput == "right":
            print("You decide to go explore the dungeon.")
            print("Hywell: I will not be able to assist you on your journey to the dungeon.")
            print("Hywell: However, please take this sword to help you on your journey.")
            print("###--- YOU HAVE BEEN GIVEN AN IRON SWORD ---###")
            print("Hywell: I wish you the best of luck!")
            print("You and Hywell part ways.")
            print("You reach the dungeon and enter it alone.")
            dungeon()
        else:
            print("Please enter a valid option.")
    

def dungeon():
    userInput= ""
    directions = ["left","right","forward"]
    print("You see the path split into 3 directions.")
    print("As you look around, you see a sign that says that the path that goes forwards leads to the boss of the dungeon.")
    print("As you have just entered the dungeon, it might not be a good idea to approach the boss.")
    while userInput not in directions:
        print("Which direction do you head towards?(left/right/forward)")
        userInput = input()
        if userInput == "left":
            print("When you enter the room, you see that it is a dead end.")
            print("You decide to go back to the beginning.")
            dungeon()
         
        elif userInput == "right":
            skeletons()

        elif userInput == "forward":
            print("Even though you think to yourself that it's a bad idea, you advance forward.")
            print("When you enter the room, you see a dragon infront of you.")
            print("You charge at the dragon but since you aren't properly prepared, you get defeated quite easily.")
            print("Dragon: FOOLISH HUMAN!")
            print("###--- GAME OVER ---###")
            print("Hint: Explore the dungeon more to find some way to defeat the boss.")
            quit()
        else:
            print("Please enter a valid option.")

def skeletons():
   userInput= ""
   options = ["run","fight"]
   print("When you enter the room, you see an army of skeletons.")
   print("You can either fight them or run.")
   print("What would you like to do?(run/fight)")
   while userInput not in options:
      userInput = input()
      if userInput == "run":
        print("You have chosen to run back to the beginning.")
        dungeon()
      elif userInput == "fight":
        print("You have chosen to fight.")
        print("With your Iron Sword, you were able to defeat the army of skeletons.")
        print("However, that battle has caused your Iron Sword to become really damaged.")
        print("After beating the skeletons, you see a new path has opened up.")
        print("Do you go want to go back or head forward?(backward/forward)")
        directions = ["backward","forward"]
        while userInput not in directions:
           userInput = input()
           if userInput == "backward":
              print("You have chosen to go back to the beginning.")
              print("However, as you try to open the door, you realize that it is locked.")
              print("So, you decide to head forward instead.")
              noteRoom()
           elif userInput == "forward":
              print("You have chosen to move forward.")
              noteRoom()
           else:
              print("Please enter a valid option.")
      else:
        print("Please enter a valid option.")


def noteRoom():
   userInput= ""
   directions = ["left","right"]
   global weapon
   print("When you enter this room, you see a note on the floor.")
   print("After you read the note, you find out that between going left or right,")
   print("one of the directions will lead you to a new sword and the other will lead to more enemies.")
   print("Which direction do you pick?(left/right)")
   while userInput not in directions:
      userInput = input()
      if userInput == "left":
        print("You have chosen to go left.")
        zombies()
      elif userInput == "right":
         print("You have chosen to go right")
         print("Once you walk closer, you realize that it's just a wall.")
         print("However, once you dig at the wall, you find a new sword you can use.")
         print("###--- YOU HAVE ACQUIRED EXCALIBUR ---###")
         weapon = True
         print("With this new weapon, you decide to test it by fighting the enemies in the other room.")
         zombies()
      else:
         print("Please enter a valid option.")

def zombies():
   userInput= ""
   options = ["run","fight"]
   global weapon
   print("You encounter a room with zombies.")
   print("Do you fight or go back?(run/fight)")
   while userInput not in options:
      userInput = input()
      if userInput == "fight":
         print("You have chosen to fight.")
         if weapon:
            print("Using your new sword, you were able to defeat the zombies easily.")
            print("This gives you the confidence that you can defeat the boss.")
            print("As you look around the room you notice a sign that leads to the boss and a sign that lead to an exit.")
            print("As you have gotten this far, would you rather defeat the boss or leave the dungeon?(exit/boss)")
            options = ["exit","boss"]
            while userInput not in options:
               userInput = input()
               if userInput == "exit":
                  print("You have chosen to leave the dungeon.")
                  print("Once you leave the dungeon, you decide to use your map to head to town.")
                  print("Once you are there, you encounter your old friend Hywell.")
                  print("You tell him about your experience and how you are happy with the new sword you have acquired.")
                  print("After talking with Hywell, you decide to stay with him in town for awhile.")
                  print("After a few days, you hear the townspeople screaming that the town is being attacked.")
                  print("You go outside to look, you quickly realize that the enemies came from the same direction as the dungeon.")
                  print("Realizing that you should've fought the boss when you had the chance, you pick up Excalibur and approach the enemy.")
                  print("Once you get close, you realize that the town is being attacked by a dragon and his army.")
                  print("Dragon: YOUR TIME HAS COME HUMANS! ALL OF YOU SHALL NOW PERISH!")
                  print("You try to fight the dragon and the army but you are sadly overpowered.")
                  print("As you draw your last breath, you realize that you should've fought the dragon when you had the chance.")
                  print("###--- YOU HAVE REACHED BAD ENDING 2 ---###")
                  quit()
               elif userInput == "boss":
                  print("You have chosen to defeat the boss.")
                  boss()
               else:
                  print("Please enter a valid option.")
         else:
            print("Since your Iron Sword is worn out, it breaks while your fighting and you die.")
            print("###--- GAME OVER ---###")
            print("Hint: Try to find that new weapon before encountering these enemies.")
            quit()
      elif userInput == "run":
         print("You have chosen to go to the previous room.")
         noteRoom()
      else:
         print("Please enter a valid option.")

def boss():
   userInput= ""
   options = ["listen","fight"]
   print("You enter into the lair of the final boss.")
   print("As you walk closer, you realize that the boss is a dragon!")
   print("Dragon: HOW DARE YOU APPROACH MALTHOR THE GREAT!?")
   print("Malthor: LEAVE NOW AND I WILL SPARE YOUR LIFE! FACING ME IS ONLY WHAT A FOOL WOULD DO!")
   print("Do you listen to Malthor's warning or fight?(listen/fight)") 
   while userInput not in options:
      userInput = input()
      if userInput == "fight":
         print("You ignore Malthor's warning and get ready to fight!")
         print("Malthor: VERY WELL! DO NOT DISSAPOINT ME HUMAN!")
         print("You charge at Malthor with Excalibur.")
         print("It was a tough fight, but Malthor was defeated!")
         print("After defeating Malthor, you see that his room his filled with treasure!")
         print("You pack up all you can take and head to town.")
         print("Once you head to town, the townspeople celebrate as they aren't under the fear that Malthor will attack them.")
         print("YOU HAVE BECOME THE HERO OF THE TOWN!")
         print("###--- YOU HAVE REACHED THE GOOD ENDING ---###")
         quit()
      elif userInput == "listen":
         print("You have chosen to listen to Malthor's warning.")
         print("Malthor: GOOD CHOICE HUMAN!")
         print("As you are leaving the lair, you realized you were tricked!")
         print("Malthor releases his flame breath and kills you.")
         print("As you are drawing your last breath, you realize that you shouldn't trust your enemies.")
         print("###--- YOU HAVE REACHED BAD ENDING 3 ---###")
         quit()
      else:
         print("Please enter a valid option.")
   
         

  
def main():
        answer = input('Would you like to play the game?(yes/no)\n')

        if answer.lower() == 'yes':
            print('Let us Begin!')
            start = True
        elif answer.lower() == 'no':
            print('Okay, some other time.')
            quit()
        else:
            print("I didn't quite understand that.\n")
            main()


        while True:
            name = input("Please State Your Name:\n")
            print("Greetings, "+ name +". Let us begin our adventure!")
            introScene()


              
if __name__ == "__main__":
    main()
              
            
            

                   
