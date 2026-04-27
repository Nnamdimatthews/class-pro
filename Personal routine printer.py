Name = input("What is your name? ")

Howareyou = input("Hello " + Name + ", how are you doing? ")

if Howareyou.lower() in ["good", "great", "fine", "well"]:
    print("That's wonderful to hear, " + Name + "!welcome to your routine printer!")
else:
    if Howareyou.lower() in ["not good", "not great", "not fine", "not well"]:
        print("I'm sorry to hear that, " + Name + ". get better soon! Anyways, welcome to your routine printer!")

print(Name + "'s daily routine")

Routine1 = input("What is your first activity for the day? ")
Routine2 = input("What is your second activity for the day? ")
Routine3 = input("What is your third activity for the day? ")
Continue = input("Do you have more activities for the day? (yes/no) ")

if Continue.lower() == "yes":
    Routine4 = input("What is your fourth activity for the day? ")
    Routine5 = input("What is your fifth activity for the day? ")
    Routine6 = input("What is your sixth activity for the day? ")
    Routine7 = input("What is your seventh activity for the day? ")
    print("Your daily routine for the day is: " + Routine1 + ", " + Routine2 + ", " + Routine3 + ", " + Routine4 + ", " + Routine5 + ", " + Routine6 + ", and " + Routine7)
else:
    print("Your daily routine for the day is: " + Routine1 + ", " + Routine2 + ", and " + Routine3)