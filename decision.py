print("Welcome to the decision game!")
name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 16:
    message = ("Sorry you are not old enough to play... =(")
elif age >= 16:
    message = ("That`s great! You are old enough to play =)")

print("Hi", name, ", you are", age, "years old.", message)
if age >= 16:
    init_game = str(input("Do you want to play? (yes/no) ")).lower()
    if init_game == "no":
        print ("Oh that`s too bad =(. Have a nice day!")
    elif init_game == "yes":
        print("Cool!")
        health = 10
        print("Your inicial health is:", health, "points")
        first_choice = input("First choice: You go need to take a path. Where you go? (right/left) ").lower()
        if first_choice == "right" or "rigth":
            health -= 10
            print("""You felt into a river and you lost 10 health points.
            Your health points are:""", health, ".",
            """You lost mate.""")
        elif first_choice == "left" or "letf":
            print ("Nice! You found a road. Your health is:", health)