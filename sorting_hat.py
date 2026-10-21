print("Welcome to Hogwarts Sorting Hat")

trait = input("What best describes you? ").lower()

if trait == "brave" and "intelligent":
    print("You belong in Gryffindor or Ravenclaw!")
elif trait == ("brave" or trait == "daring") and not "loyal":
    print("You belong in Gryffindor!")
elif trait == "loyal":
    print("You belong in Hufflepuff!")
elif trait == "ambitious":
    print("You belong in Slytherin!")
else:
    print("The Sorting Hat is confused.")

bravery = int(input("On a scale of 1-10, how brave are you? "))
loyalty = int(input("On a scale of 1-10, how loyal are you? "))

if bravery >= 7 and loyalty >= 7:
    print("You are a true Gryffindor or Hufflepuff!")
